import re

def limpar_texto_wiki(texto):
    if not texto:
        return ''
    texto = re.sub(r'\{\{.*?\}\}', '', texto, flags=re.DOTALL)
    texto = re.sub(r'\[\[([^|\]]*\|)?([^\]]+)\]\]', r'\2', texto)
    texto = re.sub(r'\[\[File:[^\]]+\]\]', '', texto, flags=re.IGNORECASE)
    texto = re.sub(r'<[^>]+>', '', texto)
    texto = re.sub(r"'''?", '', texto)
    texto = texto.replace('[', '').replace(']', '')
    return texto.strip()
