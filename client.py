import pika
import json
from utility import Utility


class MetaClass(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        ''' Single ton desgin partten'''
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class RabbitMQ(object):

    def __init__(self, server, utility):
        self.server = server
        self.utility = utility
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)

    def publish(self, payloads):
        self._channel.basic_publish(
            exchange=self.server.exchange, routing_key=self.server.routing_key, body=json.dumps(payloads))
        self.utility.log(message=" Publish Message  " + str(json.dumps(payloads)))
        self._connection.close()


class RabbitMQConfigure(metaclass=MetaClass):
    def __init__(self, queue='hello', host='localhost', routing_key='hello', exchange=''):
        self.queue = queue
        self.host = host
        self.routing_key = routing_key
        self.exchange = exchange


if __name__ == '__main__':
    try:
        utilities = Utility(filename="Sender.log")
        const = utilities.data
        utilities.log(message="Process RabbitMq started")
        server = RabbitMQConfigure(
            queue=const.get("rabbitMq_queue"), host=const.get("redis_host"),
            routing_key=const.get("rabbitMq_routing_key"), exchange='')
        rabbitMQ = RabbitMQ(server=server, utility=utilities)
        utilities.log(message="RabbitMq server started")
        my_dict = {1: 'apple', 2: 'ball'}
        rabbitMQ.publish(payloads=my_dict)
    except Exception as e:
        print(str(e))
