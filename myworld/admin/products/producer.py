import pika

params = pika.URLParameters('')

connection = pika.BlockingConnection(params)

channel  = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')