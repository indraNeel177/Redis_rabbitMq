import redis


class Redis_db(object):
    def __init__(self, server):
        self.server = server
        self.connection = redis.Redis(host=self.server.host, port=self.server.port, db=self.server.db,
                                      socket_timeout=self.server.socket_timeout)

    def setvalue(self, name, value):
        return self.connection.set(name, value)

    def getvalue(self, name: str):
        return self.connection.get(name)


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
