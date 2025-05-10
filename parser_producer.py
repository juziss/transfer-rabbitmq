import xml.etree.ElementTree as ET
import re
import pika

def limpar_texto_wiki(texto):
    if not texto:
        return ''
    texto = re.sub(r'\{\{.*?\}\}', '', texto, flags=re.DOTALL)
    texto = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', texto)
    texto = re.sub(r'\[\[File:[^\]]+\]\]', '', texto)
    texto = re.sub(r'<.*?>', '', texto)
    texto = re.sub(r"''+", '', texto)
    texto = texto.replace('[', '').replace(']', '')
    return texto.strip()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='artigos')

tree = ET.parse('simplewiki.xml')
root = tree.getroot()
ns = {'mw': 'http://www.mediawiki.org/xml/export-0.11/'}

for page in root.findall('mw:page', ns):
    title = page.find('mw:title', ns).text or 'Sem título'
    revision = page.find('mw:revision', ns)
    text_elem = revision.find('mw:text', ns) if revision is not None else None
    raw_text = text_elem.text if text_elem is not None else 'Sem conteúdo'
    texto_limpo = limpar_texto_wiki(raw_text)
    mensagem = f"Título: {title} | Texto: {texto_limpo[:200]}..."
    channel.basic_publish(exchange='', routing_key='artigos', body=mensagem.encode('utf-8'))
    print(f"✅ Enviado: {title}")

connection.close()
