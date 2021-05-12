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
