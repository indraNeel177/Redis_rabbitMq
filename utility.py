import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class FileSystem():
    def __init__(self):
        self.data = None

    def read(self):
        with open('C:/Users/pnaja/OneDrive/Desktop/test/Redis_rabbitMq/Redis_rabbitMq/const.json', 'r') as f:
            data = json.loads(f.read())
            self.data= data
        return self.data

            


