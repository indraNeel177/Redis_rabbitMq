import redis
from json import dumps, loads
from utility import FileSystem, Log
import logging


class MetaClass(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        ''' Single ton desgin partten'''
        if cls not in cls._instance:
            cls._instance[cls] = super(
                MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class Redis_db():
    def __init__(self, server):
        self.server = server
        self.connection = redis.Redis(host=self.server.host, port=self.server.port, db=self.server.db,
                                      socket_timeout=self.server.socket_timeout)

    def setvalue(self, name, value):
        value = dumps(value)
        return self.connection.set(name, value)

    def getvalue(self, name: str):
        return self.connection.get(name)


class RedisConfig(metaclass=MetaClass):
    def __init__(self, host='localhost', port=6379,
                 db=0, password=None, socket_timeout=None):
        self.host = host
        self.port = port
        self.db = db
        self.socket_timeout = socket_timeout


if __name__ == '__main__':
    try:
        const = FileSystem().read()
        log = Log(filename="Redis.log")
        log.log(message="Process redis started")
        server = RedisConfig(host=const.get("redis_host"), port=const.get("redis_port"),
                             db=const.get("redis_db"), password=const.get("redis_password"),
                             socket_timeout=None)

        redis_c = Redis_db(server=server)
        log.log(message="Redis server started")
        my_dict = {1: 'apple', 2: 'ball'}
        log.log(message="Redis Set value to database {}".format(str(my_dict)))
        redis_c.setvalue(name="pydict", value=my_dict)
        get = redis_c.getvalue(name="pydict")
        log.log(message="The value got is {}".format(str(my_dict)))
    except Exception as e:
        print(e)
        log = Log(filename="Redis.log")
        log.log(message="Redis server error  "+str(e))