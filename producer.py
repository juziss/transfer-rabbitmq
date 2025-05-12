import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='artigos')

mensagem = 'Título: Alan Turing | Texto: Alan Turing foi um matemático britânico...'

channel.basic_publish(exchange='',
                      routing_key='artigos',
                      body=mensagem)

print("✅ Mensagem enviada ao RabbitMQ!")

connection.close()
