import datetime
import json
import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class FileSystem(object):
    def __init__(self):
        self.data = None

    def read(self):
        with open(BASE_DIR + "/Redis_rabbitMq/Config.json", 'r') as f:
            data = json.loads(f.read())
            self.data = data
        return self.data


class Log(object):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        start = datetime.datetime.now()
        path = FileSystem().read().get("log_file_path")
        logging.basicConfig(filename=path + str(self.filename), level=logging.INFO)
        logging.info(msg='''{}  
               {}'''.format(str(start), str(message)))
