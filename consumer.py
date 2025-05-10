import pika

def callback(ch, method, properties, body):
    print("📥 Mensagem recebida:")
    print(body.decode('utf-8'))
    print("-" * 40)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='artigos')

channel.basic_consume(queue='artigos', on_message_callback=callback, auto_ack=True)
print("🚀 Aguardando mensagens. Pressione CTRL+C para sair.")
channel.start_consuming()
