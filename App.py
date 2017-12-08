# coding=utf8
import json

from flask import Flask, request

import MediaType
import Task
import main
import producer

app = Flask(__name__)


@app.route('/sendMsg')
def sendMsg():
    msg = request.args.get('msg')
    name = request.args.get('name')

    if not msg:
        return "msg should not be null"

    username = None
    if name:
        username = main.findByName(name=name)
    if not username:
        username = main.findRoomByName(name=name)

    print(username)

    if not username:
        username = name

    message = {'username': username, 'messsage': msg, 'mediaType': MediaType.Text}

    producer.emit(json.dumps(message, ensure_ascii=False))

    return "sendTo {username}: {msg}".format(username=username, msg=msg)


@app.route('/sendImg', methods=['POST'])
def sendImg():
    msg = request.form.get('msg')
    name = request.form.get('name')

    if not msg:
        return "msg should not be null"

    username = None
    if name:
        username = main.findByName(name=name)
    if not username:
        username = main.findRoomByName(name=name)

    print(username)

    if not username:
        username = name

    message = {'username': username, 'messsage': msg, 'mediaType': MediaType.Picture}

    producer.emit(json.dumps(message, ensure_ascii=False))

    return "sendTo {username}: {msg}".format(username=username, msg=msg)


if __name__ == '__main__':
    Task.start()
    app.run(host='0.0.0.0')
