import pika
import json
import os
import sys
from utility import FileSystem

class MetaClass(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        ''' Single ton desgin partten'''
        if cls not in cls._instance:
            cls._instance[cls] = super(
                MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class RabbitMqServerConfigure(metaclass=MetaClass):

    def __init__(self, host="localhost", queue='hello'):
        self.queue = queue
        self.host = host


class RabbitMqServer():
    def __init__(self, server):
        self.server = server
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)

    
    def callback(self,ch,method, properties, body):
        print(" [x] Received %r" % json.loads(body))

    def start_server(self):
        self._channel.basic_consume(
            queue=self.server.queue, on_message_callback=self.callback, auto_ack=True)
        self._channel.start_consuming()


if __name__ == '__main__':
    try:
        const = FileSystem().read()
        server = RabbitMqServerConfigure(queue=const.get("rabbitMq_queue"), host=const.get("redis_host"))
        rabbitMq = RabbitMqServer(server=server)
        rabbitMq.start_server()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
