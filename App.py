# coding=utf8
import json

from flask import Flask, request

import Task
import main
import producer

app = Flask(__name__)


@app.route('/sendMsg')
def sendMsg():
    msg = request.args['msg']
    name = main.findByName(name='AndyBob')
    message = {'name': name, 'messsage': msg}
    producer.emit(json.dumps(message, ensure_ascii=False))
    return "ok"


if __name__ == '__main__':
    Task.start()

    app.run(host='0.0.0.0')
