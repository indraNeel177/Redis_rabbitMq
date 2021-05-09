import sys
import json
import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class FileSystem():
    def __init__(self):
        self.data = None

    def read(self):
        with open(BASE_DIR + "/Redis_rabbitMq/Config.json", 'r') as f:
            data = json.loads(f.read())
            self.data = data
        return self.data

# class Logging():
#     def __init__(self):
#         self.filename = FileSystem().read().get("log_file_path")+ str("Redis.log")
#
#     def log(self):
#         return logging.basicConfig(filename=self.filename, filemode='w', level=logging.INFO,
#                                            format='%(name)s - %(levelname)s - %(message)s')
