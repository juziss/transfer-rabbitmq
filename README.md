# Wikipedia Parser com RabbitMQ

Este projeto realiza o parsing de artigos da Wikipedia (arquivo XML), extrai informações relevantes e envia mensagens para uma fila RabbitMQ, onde um cliente consumidor lê e exibe os dados. O objetivo é demonstrar a troca de dados assíncrona entre sistemas por meio de mensageria.

## Requisitos

- Python 3.8+
- RabbitMQ em execução local (localhost)
- Dependências:
  - pika

Para instalar as dependências:
pip install -r requirements.txt


## Execução

### 1. Iniciar o RabbitMQ

Certifique-se de que o RabbitMQ está em execução no endereço `localhost:5672`. A interface web, se disponível, pode ser acessada em `http://localhost:15672`.

### 2. Enviar artigos (produtor)

Execute o script `parser_producer.py` para:

- Ler e fazer parsing do arquivo XML
- Limpar o conteúdo dos artigos
- Enviar os dados para a fila `artigos`


### 3. Consumir mensagens (consumidor)

Execute o script `consumer.py` em um terminal separado para receber e exibir as mensagens da fila.



