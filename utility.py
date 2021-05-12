import datetime
import json
import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class Utility(object):
    def __init__(self, filename=None):
        self.filename = filename
        self.datetime = datetime.datetime.now()
        with open(BASE_DIR + "/Redis_rabbitMq/Config.json", 'r') as f:
            data = json.loads(f.read())
            self.data = data

    def log(self, message):
        try:
            path = self.data.get("log_file_path")
            logging.basicConfig(filename=path + str(self.filename), level=logging.INFO)
            logging.info(msg='''{} : {}'''.format(str(self.datetime), str(message)))
        except Exception as e:
            print(e)
            path = self.data.get("log_file_path")
            logging.basicConfig(filename=path + str("error.log"), level=logging.INFO)
            logging.info(msg='''{} : {}'''.format(str(self.datetime), str(e)))


class MetaClass(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        ''' Single ton desgin partten'''
        if cls not in cls._instance:
            cls._instance[cls] = super(
                MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class RedisConfig(metaclass=MetaClass):
    def __init__(self, host='localhost', port=6379,
                 db=0, password=None, socket_timeout=None):
        self.host = host
        self.port = port
        self.db = db
        self.socket_timeout = socket_timeout


class RabbitMqServerConfigure(metaclass=MetaClass):

    def __init__(self, host="localhost", queue='hello'):
        self.queue = queue
        self.host = host


class RabbitMQConfigure(metaclass=MetaClass):
    def __init__(self, queue='hello', host='localhost', routing_key='hello', exchange=''):
        self.queue = queue
        self.host = host
        self.routing_key = routing_key
        self.exchange = exchange
