import threading

import itchat

import comsumer
import json


def login():
    itchat.auto_login(hotReload=True,picDir='/ky/xuwuqiang/qrcode.png' )


def callback(ch, method, properties, body):
    data = json.loads(body.decode("utf-8"))
    name = data['name']
    message = data['messsage']
    if name and message:
        itchat.send_msg(msg=message, toUserName=name)
        print(" [x] %r" % body)


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    comsumer.comsume()
    print('thread %s ended.' % threading.current_thread().name)


def start():
    login()
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='wechat_sender')
    t.start()
    print('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    start()
