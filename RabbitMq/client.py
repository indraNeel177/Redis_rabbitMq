import json

import pika


class RabbitMQ(object):

    def __init__(self, server):
        self.server = server
        # self.utility = utility
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)

    def publish(self, payloads):
        self._channel.basic_publish(
            exchange=self.server.exchange, routing_key=self.server.routing_key, body=json.dumps(payloads))
        # self.utility.log(message=" Publish Message  " + str(json.dumps(payloads)))
        print("Publish Message  " + str(json.dumps(payloads)))
        self._connection.close()


class MetaClass(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        ''' Single ton desgin partten'''
        if cls not in cls._instance:
            cls._instance[cls] = super(
                MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class RabbitMQConfigure(metaclass=MetaClass):
    def __init__(self, queue='hello', host='localhost', routing_key='hello', exchange=''):
        self.queue = queue
        self.host = host
        self.routing_key = routing_key
        self.exchange = exchange
