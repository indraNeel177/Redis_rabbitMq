import datetime
# import json
import os
import sys

# import logging
# import pymysql
from yaml import load, FullLoader, YAMLError

from RabbitMq.client import RabbitMQ, RabbitMQConfigure
from RabbitMq.reciver import RabbitMqServer, RabbitMqServerConfigure
from Redis.red import Redis_db, RedisConfig

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class Utility(object):
    def __init__(self, filename=None):
        self.filename = filename
        self.datetime = datetime.datetime.now()
        with open(r'env.yaml') as file:
            try:
                const = load(file, Loader=FullLoader)
                self._const = const.get("Test")
            except YAMLError as exe:
                print(exe)
        self._redis_connection = RedisConfig(host=self._const.get("redis_host"), port=self._const.get("redis_port"),
                                             db=self._const.get("redis_db"), password=self._const.get("redis_password"),
                                             socket_timeout=None)
        self.redis = Redis_db(server=self._redis_connection)
        self._client_server = RabbitMQConfigure(
            queue=const.get("rabbitMq_queue"), host=const.get("redis_host"),
            routing_key=const.get("rabbitMq_routing_key"), exchange='')
        self._recivcer_server = RabbitMqServerConfigure(queue=const.get("rabbitMq_queue"), host=const.get("redis_host"))

    def publish(self, my_dict):
        rabbitMQ = RabbitMQ(server=self._client_server)
        # my_dict = {1: 'apple', 2: 'ball'}
        rabbitMQ.publish(payloads=my_dict)

    def consume(self):
        RabbitMqServer(server=self._recivcer_server)

    # def log(self, message):
    #     try:
    #         path = self.data.get("log_file_path")
    #         logging.basicConfig(filename=path + str(self.filename), level=logging.INFO)
    #         logging.info(msg='''{} : {}'''.format(str(self.datetime), str(message)))
    #     except Exception as e:
    #         print(e)
    #         path = self.data.get("log_file_path")
    #         logging.basicConfig(filename=path + str("error.log"), level=logging.INFO)
    #         logging.info(msg='''{} : {}'''.format(str(self.datetime), str(e)))

# class DbConfigure(metaclass=MetaClass):
#     def __init__(self, host='localhost', user='root', password="root", db='AviLeap', port=3306):
#         self.user = user
#         self.host = host
#         self.db = db
#         self.password = password
#         self.port = port

# class DB(object):
#     def __init__(self, server):
#         self.server = server
#         self.connection = pymysql.connect(host=self.server.host, user=self.server.user, password=self.server.password,
#         db=self.server.db, port=self.server.port)
#         self.cursor = self.connection.cursor()
#
#     def query(self, query):
#         self.cursor.execute(query)
#         output = self.cursor.fetchall()
#         return output
