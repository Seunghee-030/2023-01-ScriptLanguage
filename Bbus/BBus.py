'''
BBus.py
프로그램의 메인모듈

functions
- InitScreen

'''
import xml.etree.ElementTree as ET

# === XML import ===
import requests  # pip install requests

import server
import map
from book_mark import *
from link import *
# === import ===
import tkinter.ttk
from server import window
from tkinter import messagebox
import graph

# ==== 필요한 전역 변수 선언 ====
# 각 사이트 인증키
cityList = server.city_list

TempFont = font.Font(window, size=25, weight='bold', family='DungGeunMo')
smallFont = font.Font(window, size=10, weight='bold', family='DungGeunMo')
standardFont = font.Font(window, size=15,  family='DungGeunMo')
mainFont = font.Font(window, size=50, weight='bold', family='DungGeunMo', slant='italic')
listFont = font.Font(window, size=25, family='DungGeunMo')


# ====시/군 버튼 push====
# 시/군 검색 윈도우 open
def open_city_window():
    # === window 정리 ===
    clear_window()
    window.title("시/군 검색 기능")

    # === 윈도우의 기본 디자인 ===
    Label(window, text="[ 시 / 군 검색 기능 ]", font=TempFont, compound='center', bg='#000fa3', fg='white').place(x=300, y=10, width=400, height=40)
    Button(window, text="[ 시 / 군 ]", font=smallFont, compound='center', bg='#b8b8b8', fg='black',relief='raised', command=open_city_window).place(x=60, y=757, width=100, height=40)

    # === 유도 멘트 제공 ===
    Label(window, text="[ SYSTEM ] :  검색할 도시를 선택하세요 _", font=standardFont,  bg='#000fa3', fg='white', anchor='w').place(
        x=40, y=90, width=450, height=60)

    # === [cityList]의 데이터를 이용해 [city_selectListBox]와 그와 연결되는 [city_SLB_scrollbar] 생성 ===
    global city_selectListBox
    city_selectListBox = Listbox(window, font=listFont, activestyle='underline', bd=10, selectborderwidth=3, selectbackground='#000fa3', bg='#b8b8b8')
    city_selectListBox.place(x=50, y=150, width=440, height=300)

    city_SLB_scrollbar = Scrollbar(window)
    city_SLB_scrollbar.place(x=460, y=162, width=20, height=276)

    city_selectListBox.config(yscrollcommand=city_SLB_scrollbar.set)
    city_SLB_scrollbar.config(command=city_selectListBox.yview)

    # === 리스트 박스[city_selectListBox] 원소 채우기 ===
    for i, item in enumerate(cityList, start=1):
        city_selectListBox.insert(i + 1, item)

    # === 검색 버튼 - 일시적인 사용이므로 변수 제작하지 않음 ===
        # === [search_city] 함수로 이동 ===
    server.isStation = False
    Button(window, image=server.smallSearchImage, bg="white", activebackground="dark grey", relief="flat",
           cursor="hand2", command=search_station_with_citySLB).place(x=190, y=450, width=150, height=60)

# search_station_with_selectCity() : 시/군 검색어 선택 및 검색어 기준으로 정류장 리스트 생성하는 함수
def search_station_with_citySLB():
    # === 검색어 [citySLB]에서 받아오기 ===
    global city_selectListBox, station_selectListBox
    if city_selectListBox.curselection():
        server.cityInfo = cityList[city_selectListBox.curselection()[0]]
    else:
        messagebox.showinfo("알림", "검색어가 존재하지 않습니다!")
        return
    # === 선택하지 않았을 때, 경고 메시지 - 만들어야 함 !!! ===

    if not server.isStation:
        # === 추가 설명 Label ===
        Label(window, text="======================================================================", font=standardFont, bg='#000fa3',
              fg='white', anchor='w').place(x=40, y=500, width=450, height=60)
        Label(window, text="[ SYSTEM ] :  검색어 - "+ server.cityInfo, font=standardFont, bg='#000fa3',
              fg='white', anchor='w').place(x=40, y=550, width=400, height=60)
        Label(window, text="[ SYSTEM ] :  잠시만 기다려 주세요... _ ", font=standardFont, bg='#000fa3',
              fg='white', anchor='w').place(x=40, y=620, width=400, height=60)
    else:
        Label(window, text="[ SYSTEM ] :  검색어 - "+ server.cityInfo, font=standardFont, bg='#000fa3',
              fg='white', anchor='w').place(x=40, y=600, width=400, height=60)
        Label(window, text="[ SYSTEM ] :  잠시만 기다려 주세요... _ ", font=standardFont, bg='#000fa3',
              fg='white', anchor='w').place(x=40, y=670, width=400, height=60)

    # === 유도 멘트 제공 ===
    Label(window, text="[ SYSTEM ] :  검색할 정류장을 선택하세요 _", font=standardFont,  bg='#000fa3', fg='white', anchor='w').place(
        x=510, y=90, width=450, height=60)

    # === 검색어[server.cityInfo] 기준으로 경기도 버스 정류소 현황 데이터 load ===
    url_busStation = 'https://openapi.gg.go.kr/BusStation?'
    params_busStation = {'KEY': server.gggokrKey, 'pSize': '1000', 'pIndex': '1', 'SIGUN_NM' : server.cityInfo}

    response = requests.get(url_busStation, params=params_busStation)
    root = ET.fromstring(response.text)
    this_city_stations = root.findall("row")

    # === [server.cityInfo] 기준으로 버스 정류소 리스트 생성 ===
    # === 스크롤바[stationSLB_yscrollbar, stationSLB_xscrollbar] 및 리스트 박스[station_selectListBox] 위치 지정 ===
    station_selectListBox = Listbox(window, font=standardFont, activestyle='underline', bd=10, selectborderwidth=3, selectbackground='#000fa3', bg='#b8b8b8')
    station_selectListBox.place(x=510, y=150, width=440, height=500)

    stationSLB_yscrollbar = Scrollbar(window)
    stationSLB_yscrollbar.place(x=920, y=162, width=20, height=478)

    stationSLB_xscrollbar = Scrollbar(window, orient='horizontal')
    stationSLB_xscrollbar.place(x=522, y=620, width=399, height=20)

    station_selectListBox.config(yscrollcommand=stationSLB_yscrollbar.set, xscrollcommand=stationSLB_xscrollbar)
    stationSLB_yscrollbar.config(command=station_selectListBox.yview)
    stationSLB_xscrollbar.config(command=station_selectListBox.xview)

    # === 리스트 박스[station_selectListBox] 원소 채우기 ===
    for i, item in enumerate(this_city_stations, start=1):
        str = server.cityInfo + " " + item.findtext("STATION_NM_INFO")
        station_selectListBox.insert(i + 1, str)


    # === 버튼 누르면 정류장의 상세 정보 출력을 위해 준비하는 함수로 이동 [readyto_search_BusStation_fromCity]===
    Button(window, image=server.smallSearchImage, bg="white", activebackground="dark grey", relief="flat",
           cursor="hand2", command=readyto_search_busStationInfo_fromCity).place(x=800, y=650, width=150, height=60)




def readyto_search_busStationInfo_fromCity():
    global station_selectListBox
    if station_selectListBox.curselection():
        server.stationInfo = station_selectListBox.get(station_selectListBox.curselection())[4:]
    else:
        messagebox.showinfo("알림", "검색어가 존재하지 않습니다!")
        return

    # 윈도우 정리하기
    clear_window()

    Label(window, text="[ SYSTEM ] " +server.stationInfo + " 정류장에 대한 정보입니다.", font=standardFont, bg='#000fa3', fg='white', anchor='w', wraplength=400).place(
        x=40, y=90, width=450, height=60)
    Label(window, text="[ 시 / 군 검색 기능 ]", font=TempFont, compound='center', bg='#000fa3', fg='white').place(x=300, y=10, width=400, height=40)
    Button(window, text="[ 시 / 군 ]", font=smallFont, compound='center', bg='#b8b8b8', fg='black', relief='raised',
           command=open_city_window).place(x=60, y=757, width=100, height=40)

    search_busStationInfo()

# ====정류장 버튼 push====
# 정류장 검색 윈도우 open
def open_busStation_window():
    # === window 정리 ===
    clear_window()
    window.title("정류소 검색 기능")

    # === 윈도우의 기본 디자인 ===
    Label(window, text="[ 정류소 검색 기능 ]", font=TempFont, compound='center', bg='#000fa3', fg='white').place(x=300, y=10, width=400, height=40)
    Button(window, text="[ 정류소 ]", font=smallFont, compound='center', bg='#b8b8b8', fg='black', relief='raised', command=open_busStation_window).place(x=60, y=757, width=100, height=40)

    # === 유도 멘트 제공 ===
    Label(window, text="[ SYSTEM ] :  검색할 도시를 선택하세요 _", font=standardFont,  bg='#000fa3', fg='white', anchor='w').place(x=40, y=90, width=450, height=60)

    # === [cityList]의 데이터를 이용해 [city_selectListBox]와 그와 연결되는 [city_SLB_scrollbar] 생성 ===
    global city_selectListBox
    city_selectListBox = Listbox(window, font=listFont, activestyle='underline', bd=10, selectborderwidth=3,
                                 selectbackground='#000fa3', bg='#b8b8b8')
    city_selectListBox.place(x=50, y=150, width=440, height=300)

    city_SLB_scrollbar = Scrollbar(window)
    city_SLB_scrollbar.place(x=460, y=162, width=20, height=276)

    city_selectListBox.config(yscrollcommand=city_SLB_scrollbar.set)
    city_SLB_scrollbar.config(command=city_selectListBox.yview)

    # === 리스트 박스[city_selectListBox] 원소 채우기 ===
    for i, item in enumerate(cityList, start=1):
        city_selectListBox.insert(i + 1, item)

    # === 추가 설명 Label ===
    Label(window, text="[ SYSTEM ] :  정류장을 입력하세요 _ ", font=standardFont, bg='#000fa3',
          fg='white', anchor='w').place(x=40, y=450, width=400, height=60)
    Label(window, text="[  USER  ] :", font=standardFont, bg='#000fa3',
          fg='white', anchor='w').place(x=40, y=500, width=150, height=40)

    # === 시/군 검색어 입력 창 ===
    global busStation_search_text
    busStation_search_text = Text(window, height=1, width=30, font=standardFont, bg='#000f87', fg='white', relief='flat')
    busStation_search_text.place(x=180, y=508)


    # === 검색 버튼 - 일시적인 사용이므로 변수 제작하지 않음. ===
    server.isStation = True
    Button(window, image=server.smallSearchImage, bg="white", activebackground="dark grey", relief="flat",
           cursor="hand2", command=readyto_search_busStation).place(x=350, y=530, width=150, height=60)
    Button(window, image=server.stationList, bg="white", activebackground="dark grey", relief="flat",
           cursor="hand2", command=search_station_with_citySLB).place(x=30, y=530, width=150, height=60)

def readyto_search_busStation():
    global city_selectListBox, busStation_search_text
    if city_selectListBox.curselection():
        server.stationInfo = busStation_search_text.get("1.0", END).strip()
        server.cityInfo = cityList[city_selectListBox.curselection()[0]]
    else:
        messagebox.showinfo("알림", "검색어가 존재하지 않습니다!")
        return

    if server.stationInfo == "":
        messagebox.showinfo("알림", "검색어가 존재하지 않습니다!")
        return


    # === 추가 설명 Label ===
    Label(window, text="======================================================================", font=standardFont, bg='#000fa3',
          fg='white', anchor='w').place(x=40, y=580, width=450, height=60)
    Label(window, text="[ SYSTEM ] : " + server.stationInfo +" 정류장 버스 목록을 불러오는 중입니다...", font=standardFont, bg='#000fa3',
          fg='white', anchor='w', wraplength=400).place(x=40, y=650, width=400, height=60)
    search_busStationInfo()

# search_busStationInfo() : 정류장 검색어 기준으로 정류장에 도착하는 버스 목록 생성하는 함수
def search_busStationInfo():
    # === 검색어 입력 ===
    print("검색어:", server.stationInfo)

    # === 검색어[server.cityInfo] 기준으로 경기도 버스 정류소 현황 데이터 load ===
    url_busStation = 'https://openapi.gg.go.kr/BusStation?'
    params_busStation = {'KEY': server.gggokrKey, 'pSize': '1000', 'pIndex': '1', 'SIGUN_NM': server.cityInfo}

    response = requests.get(url_busStation, params=params_busStation)
    root = ET.fromstring(response.text)
    items = root.findall("row")

    # === [server.cityInfo] 기준으로 받아온 데이터와 [정류장명]이 같은 경우의 [정류장ID] 및 [위도/경도] 받아오기 ===
    station_id = ""
    for i, item in enumerate(items, start=1):
        if server.stationInfo == item.findtext("STATION_NM_INFO"):
            station_id = item.findtext("STATION_ID")
            server.latitude = float(item.find("WGS84_LAT").text)
            server.longitude = float(item.find("WGS84_LOGT").text)

            server.memo_text = '\n\n[정류장 ID]' + item.findtext("STATION_ID")
            server.memo_text += '\n\n[지역]' + item.findtext("SIGUN_NM")
            server.memo_text += '\n\n[정류장명(한글)]' + item.findtext("STATION_NM_INFO")
            server.memo_text += '\n\n[정류장명(영문)]' + item.findtext("ENG_STATION_NM_INFO")

    if station_id == "":
        messagebox.showinfo("알림", server.stationInfo + " 정류장이 존재하지 않습니다!")
        return
    global busArrival_items
    # === 검색어[station_id] 기준으로 경기도 버스 도착 정보 조회 데이터 load  ===
    url_busArrival = 'http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalList?'
    params_busArrival = {'serviceKey': server.datagokrKey, 'stationId': station_id}

    busArrival_response = requests.get(url_busArrival, params=params_busArrival)
    busArrival_root = ET.fromstring(busArrival_response.text)
    busArrival_items = busArrival_root.findall(".//busArrivalList")

    # === 해당 정류소 북마크에 저장 ===
    Button(window, image=server.boomarkImage, bg='#000fa3', activebackground="dark grey", relief="flat",
           cursor="hand2", command=makeBookMark).place(x=920, y=480, width=50, height=50)

    # === [station_id] 기준으로 해당 정류장에 도착하는 리스트 생성 ===
    # === 스크롤바[sbusSLB_scrollbar] 및 리스트 박스[busStation_searchListBox] 위치 지정 ===

    # === [server.cityInfo] 기준으로 버스 정류소 리스트 생성 ===
    # === 스크롤바[stationSLB_yscrollbar, stationSLB_xscrollbar] 및 리스트 박스[station_selectListBox] 위치 지정 ===
    bus_selectListBox = Listbox(window, font=listFont, activestyle='underline', bd=10, selectborderwidth=3,
                                    selectbackground='#000fa3', bg='#b8b8b8')
    bus_selectListBox.place(x=510, y=150, width=440, height=300)

    busSLB_yscrollbar = Scrollbar(window)
    busSLB_yscrollbar.place(x=920, y=162, width=20, height=278)

    busSLB_xscrollbar = Scrollbar(window, orient='horizontal')
    busSLB_xscrollbar.place(x=522, y=420, width=399, height=20)

    bus_selectListBox.config(yscrollcommand=busSLB_yscrollbar.set, xscrollcommand=busSLB_xscrollbar)
    busSLB_yscrollbar.config(command=bus_selectListBox.yview)
    busSLB_xscrollbar.config(command=bus_selectListBox.xview)

    # === [busStation_searchListBox]에서 목록 선택 시, 이벤트 발생 ===
    bus_selectListBox.bind('<<ListboxSelect>>', setBus)

    # === 검색어 [루트ID] 기준으로 경기도 버스 노선 조회 데이터 load ===
    url_busRoute = 'http://apis.data.go.kr/6410000/busrouteservice/getBusRouteInfoItem'

    # === 해당 [station_id]를 경유하는 [routeID]의 노선 번호 및 여러 데이터 [busStation_searchListBox]에 저장하기 ===
    global busRoutes_items
    busRoutes_items = [server.stationInfo]
    busItems_toGraph = []
    for i, item in enumerate(busArrival_items, start=1):
        params_busRoute = {'serviceKey': server.datagokrKey, 'routeId': item.findtext("routeId")}

        busRoute_response = requests.get(url_busRoute, params=params_busRoute)
        busRoute_root = ET.fromstring(busRoute_response.text)
        busRoutes_items.append(busRoute_root.findall(".//busRouteInfoItem"))

        str = busRoutes_items[i][0].findtext("routeName") + "번 버스"
        bus_selectListBox.insert(i, str)

        if item.findtext("predictTime2") == '':
            busItems_toGraph.append((busRoutes_items[i][0].findtext("routeName"), 1))
        else:
            busItems_toGraph.append((busRoutes_items[i][0].findtext("routeName"), 2))

    # === 그래프로 현재 정류장에 도착할 버스 종류와, 개수 그림 ===
    graph.drawGraph(busItems_toGraph, window)

# 도착 정보 출력
def show_busStationInfo() :
    # === busRoute_items에서 해당 버스의 실시간 도착 정보 제공 ===
    global busRoutes_items, busArrival_items
    str = busRoutes_items[server.busInfo + 1][0].findtext("routeName") + "번 버스\n\n"

    if busArrival_items[server.busInfo].findtext("predictTime1") != '':
        str += busArrival_items[server.busInfo].findtext("predictTime1") + "분 후 도착 예정\n"

    if busArrival_items[server.busInfo].findtext("predictTime2") != '':
        str += busArrival_items[server.busInfo].findtext("predictTime2") + "분 후 도착 예정"

    Button(window, font=listFont, image=server.busInfoImage, wraplength=400, command=readyto_search_busRoute_fromStation).place(x=580, y=480, width=300, height=205)
    Label(window, font=standardFont, text=str, wraplength=400, bg='#b8b8b8').place(x=605, y=505, width=250, height=155)

    # === 지도 아이콘 선택 ===
    Button(window, image=server.mapImage, bg="white", activebackground="dark grey", relief="flat",
           cursor="hand2", overrelief="flat", command=map.onMapPopup).place(x=850, y=100, width=100, height=40)

# === 이벤트 발생 함수 ===
def setBus(event):                      # 정류장 선택 > 도시 선택 > 정류장명 작성 > 해당 정류장의 버스 목록 중 하나 선택 시 실행.
    tmp = event.widget.curselection()
    if tmp:
        server.busInfo = event.widget.curselection()[0]
        show_busStationInfo()


# ====버스 버튼 push ====
# 버스 검색 윈도우 open
def open_bus_window() :
    # === window 정리 ===
    clear_window()
    window.title("버스 노선 검색 기능")

    # === 윈도우의 기본 디자인 ===
    Label(window, text="[ 버스 노선 검색 기능 ]", font=TempFont, compound='center', bg='#000fa3', fg='white').place(x=300, y=10, width=400, height=40)
    Button(window, text="[ 버스 노선 ]", font=smallFont, compound='center', bg='#b8b8b8', fg='black', relief='raised', command=open_bus_window).place(x=60, y=757, width=100, height=40)

    # === 유도 멘트 제공 ===
    Label(window, text="[ SYSTEM ] :  검색할 버스 노선을 입력하세요 _", font=standardFont, bg='#000fa3', fg='white', anchor='w').place(x=40, y=90, width=450, height=60)

    # === 추가 설명 Label ===
    Label(window, text="[  USER  ] :", font=standardFont, bg='#000fa3', fg='white', anchor='w').place(x=40, y=150, width=150, height=40)

    # === 시/군 검색어 입력 창 ===
    global busRoute_search_text
    busRoute_search_text = Text(window, height=1, width=30, font=standardFont, bg='#000f87', fg='white', relief='flat')
    busRoute_search_text.place(x=180, y=158)

    # === 검색 버튼 - 일시적인 사용이므로 변수 제작하지 않음. ===
    Button(window, image=server.smallSearchImage, bg="white", activebackground="dark grey", relief="flat",
           cursor="hand2", command=readyto_search_busRoute).place(x=350, y=190, width=150, height=60)

def readyto_search_busRoute():
    global busRoute_search_text, passLoad
    server.busInfo = busRoute_search_text.get("1.0", END).strip()
    passLoad = 0
    search_bus()
def readyto_search_busRoute_fromStation():
    global busRoute_search_text, busRoutes_items, passLoad
    server.busInfo = busRoutes_items[server.busInfo + 1][0].findtext("routeId")
    passLoad = 1
    search_bus()

# 버스 검색어 입력 및 리스트 생성
def search_bus():
    global busRoute_items, passLoad
    busRoute_items = []
    if passLoad == 0:
        # === 추가 설명 Label ===
        Label(window, text="======================================================================", font=standardFont, bg='#000fa3',
              fg='white', anchor='w').place(x=40, y=240, width=450, height=60)
        Label(window, text="[ SYSTEM ] :  검색어 - " + server.busInfo, font=standardFont, bg='#000fa3',
              fg='white', anchor='w').place(x=40, y=290, width=400, height=60)
        # === [routeId]를 기준 ===
        url_busRoute = 'http://apis.data.go.kr/6410000/busrouteservice/getBusRouteList'
        params_busRoute = {
            'serviceKey': 'xmFs5IrPwwEJmSe8Pu6PcPO8P6+iVF5mfCz/yTZ3WPmUjST6KEDtbhXDh9hAil7MP4Mhgli8CiW91OzNPR5N+A==', \
            'keyword': server.busInfo}

        busRoute_response = requests.get(url_busRoute, params=params_busRoute)
        busRoute_root = ET.fromstring(busRoute_response.text)
        busRoute_items = busRoute_root.findall(".//busRouteList")

        # === [city_search_term] 기준으로 버스 정류소 리스트 생성 ===
        # === 스크롤바[city_Scrollbar] 및 리스트 박스[city_SearchListBox] 위치 지정 ===

        # === [cityList]의 데이터를 이용해 [city_selectListBox]와 그와 연결되는 [city_SLB_scrollbar] 생성 ===
        busRoute_selectListBox = Listbox(window, font=standardFont, activestyle='underline', bd=10, selectborderwidth=3,
                                     selectbackground='#000fa3', bg='#b8b8b8')
        busRoute_selectListBox.place(x=50, y=350, width=440, height=380)

        busRoute_SLB_scrollbar = Scrollbar(window)
        busRoute_SLB_scrollbar.place(x=460, y=362, width=20, height=356)

        busRoute_selectListBox.config(yscrollcommand=busRoute_SLB_scrollbar.set)
        busRoute_SLB_scrollbar.config(command=busRoute_selectListBox.yview)

        # === 리스트 박스[city_SearchListBox] 원소 채우기 ===
        for i, item in enumerate(busRoute_items, start=1):
            str = item.findtext("routeName") + " | " + item.findtext("regionName") + " | " +item.findtext("routeTypeName")
            busRoute_selectListBox.insert(i, str)
        busRoute_selectListBox.bind('<<ListboxSelect>>', show_busRouteInfo)
    else:
        # === [routeId]를 기준 ===
        url_busRoute = 'http://apis.data.go.kr/6410000/busrouteservice/getBusRouteInfoItem'
        params_busRoute = {
            'serviceKey': 'xmFs5IrPwwEJmSe8Pu6PcPO8P6+iVF5mfCz/yTZ3WPmUjST6KEDtbhXDh9hAil7MP4Mhgli8CiW91OzNPR5N+A==', \
            'routeId': server.busInfo}
        busRoute_response = requests.get(url_busRoute, params=params_busRoute)
        busRoute_root = ET.fromstring(busRoute_response.text)
        busRoute_items = busRoute_root.findall(".//busRouteInfoItem")
        print(busRoute_items[0].findtext("routeName"))

        # 정보 부분 (notebook)
        global InfoLabel, ST, notebook
        infoWindow = Tk()
        infoWindow.title("버스 노선 상세 정보")
        busRoute_notebook = tkinter.ttk.Notebook(infoWindow)
        busRoute_notebook.pack()
        style = tkinter.ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background="gray")
        style.map("TNotebook", background=[("selected", "gray")])

        ST = st.ScrolledText(infoWindow, font=server.fontInfo, cursor="arrow")
        busRoute_notebook.add(ST, text="Info")

        info = '[노선번호]' + '\n' + busRoute_items[0].findtext("routeName") + \
               '\n\n' + '[노선아이디]' + '\n' + busRoute_items[0].findtext("routeId") + \
               '\n\n' + '[노선유형명]' + '\n' + busRoute_items[0].findtext('routeTypeName') + \
               '\n\n' + '[노선지역]' + '\n' + busRoute_items[0].findtext('regionName')

        ST.configure(state="normal")  # 수정 가능으로 풀어놨다가,
        ST.delete('1.0', END)
        ST.insert(INSERT, info)
        ST.configure(state="disabled")  # 수정 불가능(읽기 전용)으로 변경


def show_busRouteInfo(event):
    global busRoute_items
    selectedBus = event.widget.curselection()[0]
    busRoute_notebook = tkinter.ttk.Notebook(window)
    busRoute_notebook.place(x=510, y=450, width=535, height=280)

    # 정보 부분 (notebook)
    global InfoLabel, ST, notebook
    style = tkinter.ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="gray")
    style.map("TNotebook", background=[("selected", "gray")])

    ST = st.ScrolledText(window, font=server.fontInfo, cursor="arrow")
    busRoute_notebook.add(ST, text="Info")

    info = '[노선번호]' + '\n' + busRoute_items[selectedBus].findtext("routeName") + \
                           '\n\n' + '[노선아이디]' + '\n' + busRoute_items[selectedBus].findtext("routeId") + \
                           '\n\n' + '[노선유형명]' + '\n' + busRoute_items[selectedBus].findtext('routeTypeName') + \
                            '\n\n' + '[노선지역]' + '\n' + busRoute_items[selectedBus].findtext('regionName')

    ST.configure(state="normal")  # 수정 가능으로 풀어놨다가,
    ST.delete('1.0', END)
    ST.insert(INSERT, info)
    ST.configure(state="disabled")  # 수정 불가능(읽기 전용)으로 변경
# 뒤로 가기 함수
def open_past_window():
    pass

# 화면 클리어 함수
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()
    Label(window, image=server.backGroundImage).place(x=0, y=0)
    Button(window, image=server.homeIcon, relief="flat",
           cursor="hand2", command=InitScreen).place(x=900, y=12, width=40, height=40)
    Button(window, image=server.markImage, relief="flat",
           cursor="hand2", command=onMarkPopup).place(x=830, y=12, width=40, height=40)


# === functions ===
def InitScreen():  # 메인 GUI 창을 시작하는 함수
    clear_window()
    # === frame arrangement ===
    # 분류 제목 레이블 부분
    mainLabel = Label(window, text="[ 메인 메뉴 ]", font=TempFont, compound='center', bg='#000fa3', fg='white')
    titleLabel = Label(window, text="# 뻐-스 (bBus)", font=mainFont, compound='center', bg='#000fa3', fg='white')
    CityLabel = Label(window, text="시 / 군", font=TempFont, compound='center', bg='#000fa3', fg='white')
    StationLabel = Label(window, text="정류소명", font=TempFont, compound='center', bg='#000fa3', fg='white')
    LineNumberLabel = Label(window, text="노선명", font=TempFont, compound='center', bg='#000fa3', fg='white')

    # 줄 맞추기 정보
    mainLabel.place(x=300, y=10, width=400, height=40)
    titleLabel.place(x=100, y=650, width=500, height=60)
    CityLabel.place(x=700, y=150, width=200, height=40)
    StationLabel.place(x=700, y=340, width=200, height=40)
    LineNumberLabel.place(x=700, y=530, width=200, height=40)

    # 로고 버튼 - git 주소 연결
    Button(window, image=server.photo, command=onLogo, relief="flat",bg="#000fa3",
           cursor="hand2", overrelief="groove").place(x=100, y=150, width=500, height=500)

    # 시/군 검색 버튼 - 시/군 검색 페이지로
    Button(window, image=server.searchImage, bg="white", activebackground="dark grey", relief="flat",
                            cursor="hand2", command=open_city_window).place(x=700, y=190, width=200, height=80)
    # 정류소 명 검색 버튼
    Button(window, image=server.searchImage, bg="white", activebackground="dark grey", relief="flat",
                            cursor="hand2", command=open_busStation_window, font=TempFont).place(x=700, y=380, width=200, height=80)
    # 노선 명 검색 버튼
    Button(window, image=server.searchImage, bg="white", activebackground="dark grey", relief="flat",
                            cursor="hand2", command=open_bus_window).place(x=700, y=570, width=200, height=80)





if __name__ == '__main__':
    print("main laucher runned\n")
    InitScreen()
    server.update_frame()    # Gif update 함수
    window.mainloop()
else:
    print("main launcher imported\n")