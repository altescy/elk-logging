import logging
import os
import random
from flask import Flask, jsonify

LOGPATH = os.environ.get('LOGPATH', '/tmp/app.log')

logging.basicConfig(filename=LOGPATH,
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
app = Flask(__name__)

@app.route('/')
def main():
    for _ in range(0, 10):
        x = random.randint(0, 2)
        if x == 0:
            app.logger.warning('this is WARNING message')
        elif x == 1:
            app.logger.critical('this is CRITICAL message')
        else:
            app.logger.error('this is ERROR message')
    return jsonify('Hello, world!')
