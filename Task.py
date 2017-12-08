import threading

import itchat

import MediaType
import comsumer
import json

from util import imageDownloader


def login():
    itchat.auto_login(hotReload=True, enableCmdQR=2)




def callback(ch, method, properties, body):
    data = json.loads(body.decode("utf-8"))
    name = data['username']
    message = data['messsage']
    mediaType = data['mediaType']
    print('receive data:',data)
    if name and message:
        if mediaType == MediaType.Text:
            itchat.send_msg(msg=message, toUserName=name)
            print(" [x] %r" % body)
        if mediaType == MediaType.Picture:
            pic = imageDownloader.downLoadImg(message)
            itchat.send_image(pic,toUserName=name)


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
