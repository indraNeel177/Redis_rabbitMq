import redis
from json import dumps


class Redis_db(object):
    def __init__(self, server):
        self.server = server
        self.connection = redis.Redis(host=self.server.host, port=self.server.port, db=self.server.db,
                                      socket_timeout=self.server.socket_timeout)

    def setvalue(self, name, value):
        value = dumps(value)
        return self.connection.set(name, value)

    def getvalue(self, name: str):
        return self.connection.get(name)
