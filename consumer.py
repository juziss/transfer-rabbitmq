import pika

def callback(ch, method, properties, body):
    print("📥 Mensagem recebida:")
<<<<<<< HEAD
    print(body.decode())

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='artigos')

channel.basic_consume(queue='artigos',
                      on_message_callback=callback,
                      auto_ack=True)

print('🔁 Aguardando mensagens. Pressione CTRL+C para sair.')
=======
    print(body.decode('utf-8'))
    print("-" * 40)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='artigos')

channel.basic_consume(queue='artigos', on_message_callback=callback, auto_ack=True)
print("🚀 Aguardando mensagens. Pressione CTRL+C para sair.")
>>>>>>> 1cd85718c02a78c660dff67958faad37fc390680
channel.start_consuming()
