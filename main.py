# coding=utf8
import itchat, time
from itchat.content import *


def serachFriend():
    me = itchat.search_friends()
    # 获取特定UserName的用户信息
    # bob = itchat.search_friends(userName='AndyBob')
    # print(bob)
    # 获取任何一项等于name键值的用户
    name = itchat.search_friends(name='AndyBob')
    contract = itchat.get_contact()
    print(contract)
    print(name)
    # 获取分别对应相应键值的用户
    # itchat.search_friends(wechatAccount='AndyBob')
    # 三、四项功能可以一同使用
    # itchat.search_friends(name='LittleCoder机器人', wechatAccount='littlecodersh')


# 文本信息
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    pass
    # itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])


def findByName(name):
    name = itchat.search_friends(name=name)
    if name:
        return name[0]['UserName']
    return None


def findRoomByName(name):
    name = itchat.search_chatrooms(name=name)
    if name:
        return name[0]['UserName']
    return None


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    # name = itchat.search_chatrooms(name='小花裙')
    # print(name)
    itchat.send_msg(toUserName=findRoomByName(name='小花裙'), msg='啦啦啦')
    # itchat.run()
