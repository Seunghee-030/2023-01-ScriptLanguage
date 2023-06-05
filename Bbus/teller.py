#!/usr/bin/python
# coding=utf-8

import time
import sqlite3
import telepot
from pprint import pprint
from datetime import date, datetime
import tkinter.messagebox as msgbox
import noti


def replySTData(STATION_param, user, SIGUN_param='군포시'):
    print("replySTData : ", user, STATION_param, SIGUN_param)
    res_list = noti.getData(SIGUN_param, STATION_param)
    msg = ''
    for r in res_list:
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1> noti.MAX_MSG_LENGTH:
            noti.sendMessage(user, msg)
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        noti.sendMessage(user, msg)
    else:
        noti.sendMessage(user, SIGUN_param + ' %s에 해당하는 정류소가 없습니다.' % STATION_param)

def save(user, STATION_param, SIGUN_param):
    conn = sqlite3.connect('telelog/users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, sigun TEXT, station TEXT, PRIMARY KEY(user, sigun, station) )')
    try:
        cursor.execute('INSERT INTO users(user, sigun, station) VALUES ("%s", "%s", "%s")' % (user, SIGUN_param, STATION_param))
    except sqlite3.IntegrityError:
        noti.sendMessage(user, '이미 해당 정보가 저장되어 있습니다.')
        return
    else:
        noti.sendMessage(user, '저장되었습니다.')
        conn.commit()

def check( user ):
    conn = sqlite3.connect('telelog/users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, sigun TEXT, station TEXT, PRIMARY KEY(user, sigun, station) )')
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall():
        row =  '시/군:' + data[2]+ ', 정류소명:' + data[1] + ', 정류소ID:' + str(data[0])
        noti.sendMessage(user, row)



def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('정류소') and len(args) > 1:
        print('try to 정류소 ', args[2])
        if len(args) != 3:
            noti.sendMessage(chat_id, '정확한 파라미터를 입력해주세요.')
        else:
            replySTData(args[2], chat_id, args[1])
    elif text.startswith('북마크확인'):
        print('try to 북마크확인')
        noti.getBookMark(chat_id)
    elif text.startswith('저장')  and len(args)>1:
        print('try to 저장 ', args[1], args[2])
        save( chat_id, args[1], args[2])
    elif text.startswith('확인'):
        print('try to 확인')
        check( chat_id )
    elif text.startswith('안녕'):
        noti.sendMessage(chat_id, '안녕하세요. 저는 경기도 버스 정보알리미 '
                                  '\n<뻐스봇> 입니다.\n'
                                  '무엇을 도와드릴까요?\n\n'
                                  '정류소 [지역이름] [정류소명] \n'
                                  '북마크확인\n'
                                  '저장 [지역이름] [정류소명]\n'
                                  '확인 \n'
                                  '중 하나의 명령을 입력하세요.')
    else:
        noti.sendMessage(chat_id, """모르는 명령어입니다.\n
        정류소 [지역이름] [정류소명] \n
        북마크확인\n
        저장 [지역이름] [정류소명]\n
        확인 \n
        중 하나의 명령을 입력하세요.\n
        """)

today = date.today()
current_month = today.strftime('%Y%m')

print( '[', today,']received token :', noti.TOKEN)

bot = telepot.Bot(noti.TOKEN)
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)