# -*- coding: utf-8 -*-
import time
import itchat

def getchatRooms():
    itchat.auto_login(True)

    rooms = itchat.get_chatrooms()
    print(rooms)
    for item in rooms:
        print(item['NickName'])

def getFriendList():
    itchat.auto_login(True)
    friends = itchat.get_friends(True)
    for friend in friends:
        print(friend.get('RemarkName'),'[',friend.get('NickName'),']')
    print(friends)

def createChatRooms():
    itchat.auto_login(True)
    bob = itchat.search_friends(name='AndyBob')[0]
    linlin = itchat.search_friends(name='琳琳')[0]
    yf = itchat.search_friends(name='o c')[0]
    wq = itchat.search_friends(name='徐武强')[0]
    zg = itchat.search_friends(name='制哥')[0]
    print(bob,wq,zg,linlin,yf)
    menber = [
    linlin,wq,yf
    ]
    for i in range(50):
        roomname = '代码尝试'+str(i)
        itchat.create_chatroom(menber, roomname)
        myroom = itchat.search_chatrooms(name=roomname)
        for n in myroom:
            name = n.get('UserName')
            itchat.send_msg(msg=str(i),toUserName=name)
            time.sleep(1)

if __name__ == '__main__':
    # createChatRooms()
    # getchatRooms()
    getFriendList()
