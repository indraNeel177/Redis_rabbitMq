import pika
import json


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
