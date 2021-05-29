import json

import pika


class RabbitMqServer(object):
    def __init__(self, server):
        self.server = server
        # self.utility = utility
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)

    def callback(self, ch, method, properties, body):
        # self.utility.log(message=" [x] Received " + str(json.loads(body)))
        return " [x] Received " + str(json.loads(body))

    def start_server(self):
        # self.utility.log(message=" Waiting to get Messages from server")
        print(" Waiting to get Messages from server")
        self._channel.basic_consume(
            queue=self.server.queue, on_message_callback=self.callback, auto_ack=True)
        self._channel.start_consuming()


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
