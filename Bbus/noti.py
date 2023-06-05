#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback
import xml.etree.ElementTree as ET
import requests
import server
import BBus
import tkinter.messagebox as msgbox
import os
import pickle

key = 'djFNBIwaWVJkvgD56MeKPoMOwQXZfH7Xf7YsT2RWf5OcKHKeOh9vJzssSBS4FfZlPWSGtpOPWp7rEUFjILX4tg' #'여기에 API KEY를 입력하세요'
TOKEN = '6068757360:AAExM9m867OHNkcSxS0SteOJTn1f-A5k2ew'
bot = telepot.Bot(TOKEN)
MAX_MSG_LENGTH = 300
station_id = ""

# === function ===

def getBookMark(chat_id):  # 피클 모듈을 사용해 북마크 목록 불러와 전송하는 함수
    dirpath = os.getcwd()
    if os.path.isfile(dirpath + '\mark'):
        f = open('mark', 'rb')
        dic = pickle.load(f)
        f.close()

        for value in dic.values():
            sendMessage(chat_id, value)

# 정류소 검색
def getData(SIGUN_param, STATION_param):
    res_list = []
    #str = ()
    global station_id
    if STATION_param.isdigit()==False:
    # === 검색어[server.cityInfo] 기준으로 경기도 버스 정류소 현황 데이터 load ===
        url_busStation = 'https://openapi.gg.go.kr/BusStation?'
        params_busStation = {'KEY': server.gggokrKey, 'pSize': '1000', 'pIndex': '1', 'SIGUN_NM': SIGUN_param}

        response = requests.get(url_busStation, params=params_busStation)
        root = ET.fromstring(response.text)
        items = root.findall("row")

    # === [server.cityInfo] 기준으로 받아온 데이터와 [정류장명]이 같은 경우의 [정류장ID] 및 [위도/경도] 받아오기 ===
        temp_str = {}
        for i, item in enumerate(items, start=1):
            if STATION_param == item.findtext("STATION_NM_INFO"):
                station_id = item.findtext("STATION_ID")

        #return str
                # === 검색어[station_id] 기준으로 경기도 버스 도착 정보 조회 데이터 load  ===
                url_busArrival = 'http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalList?'
                params_busArrival = {'serviceKey': server.datagokrKey, 'stationId': station_id}

                busArrival_response = requests.get(url_busArrival, params=params_busArrival)
                busArrival_root = ET.fromstring(busArrival_response.text)
                busArrival_items = busArrival_root.findall(".//busArrivalList")
                url_busRoute = 'http://apis.data.go.kr/6410000/busrouteservice/getBusRouteInfoItem'

                # === 해당 [station_id]를 경유하는 [routeID]의 노선 번호 및 여러 데이터 [busStation_searchListBox]에 저장하기 ===
                global busRoutes_items
                busRoutes_items = [station_id]
                for i, item in enumerate(busArrival_items, start=1):

                    params_busRoute = {'serviceKey': server.datagokrKey, 'routeId': item.findtext("routeId")}

                    busRoute_response = requests.get(url_busRoute, params=params_busRoute)
                    busRoute_root = ET.fromstring(busRoute_response.text)
                    busRoutes_items.append(busRoute_root.findall(".//busRouteInfoItem"))
                    route_id = busRoutes_items[i][0].findtext("routeId")
                    info = '[노선이름]' + '\n' + busRoutes_items[i][0].findtext("routeName") + \
                           '\n' + '[운행지역]' + '\n' + busRoutes_items[i][0].findtext("regionName") + \
                           '\n' + '[노선ID]' + '\n' + busRoutes_items[i][0].findtext("routeId")
                    res_list.append(info)

                    if item.findtext("predictTime1") != '':
                        res_list.append(item.findtext("predictTime1") + "분 후 도착 예정\n")

                    if item.findtext("predictTime2") != '':
                        res_list.append(item.findtext("predictTime2") + "분 후 도착 예정")
    else:
        res_list = ''
    return res_list

# 도착 정보 출력
def getArrivalData(param, date_param):
    res_list = []


def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def run(date_param, param='11710'):
    conn = sqlite3.connect('../../Telegram_Bot_BBus_EX/logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('../../Telegram_Bot_BBus_EX/users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user, param = data[0], data[1]
        print(user, date_param, param)
        res_list = getData( param, date_param )
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user,log) VALUES ("%s", "%s")'%(user,r))
            except sqlite3.IntegrityError:
                # 이미 해당 데이터가 있다는 것을 의미합니다.
                pass
            else:
                print( str(datetime.now()).split('.')[0], r )
                if len(r+msg)+1>MAX_MSG_LENGTH:
                    sendMessage( user, msg )
                    msg = r+'\n'
                else:
                    msg += r+'\n'
        if msg:
            sendMessage( user, msg )
    conn.commit()

if __name__=='__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')

    print( '[',today,']received token :', TOKEN )

    print( bot.getMe() )

    run(current_month)
