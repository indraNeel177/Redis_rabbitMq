from utility import Utility, RabbitMQConfigure, RabbitMqServerConfigure, RedisConfig
from red import Redis_db
from client import RabbitMQ
from reciver import RabbitMqServer
from json import loads


class Main(object):

    def redis(self, filename):
        utilities = Utility(filename=filename)
        const = utilities.data
        utilities.log(message="Process redis started")
        server = RedisConfig(host=const.get("redis_host"), port=const.get("redis_port"),
                             db=const.get("redis_db"), password=const.get("redis_password"),
                             socket_timeout=None)
        redis_c = Redis_db(server=server)
        utilities.log(message="Redis server started")
        my_dict = {1: 'apple', 2: 'ball'}
        utilities.log(message="Redis Set value to database {}".format(str(my_dict)))
        redis_c.setvalue(name="pydict", value=my_dict)
        get = loads(redis_c.getvalue(name="pydict"))
        utilities.log(message="The value got is {}".format(str(get)))

    def RabbitMqClient(self, filename):
        utilities = Utility(filename=filename)
        const = utilities.data
        utilities.log(message="Process RabbitMq started")
        server = RabbitMQConfigure(
            queue=const.get("rabbitMq_queue"), host=const.get("redis_host"),
            routing_key=const.get("rabbitMq_routing_key"), exchange='')
        rabbitMQ = RabbitMQ(server=server, utility=utilities)
        utilities.log(message="RabbitMq server started")
        my_dict = {1: 'apple', 2: 'ball'}
        rabbitMQ.publish(payloads=my_dict)

    def RabbitMqServer(self, filename):
        utilities = Utility(filename=filename)
        const = utilities.data
        utilities.log(message="Process RabbitMq started")
        server = RabbitMqServerConfigure(queue=const.get("rabbitMq_queue"), host=const.get("redis_host"))
        rabbitMq = RabbitMqServer(server=server, utility=utilities)
        utilities.log(message="RabbitMq server started")
        rabbitMq.start_server()


if __name__ == '__main__':
    try:
        main = Main()
        main.redis(filename="Redis.log")
        main.RabbitMqClient(filename="Client.log")
        main.RabbitMqServer(filename="Receiver.log")
    except Exception as e:
        print(e)
        utilities = Utility(filename="error.log")
        utilities.log(message="Error " + str(e))
