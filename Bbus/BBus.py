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

# ==== 필요한 전역 변수 선언 ====
# 각 사이트 인증키
cityList = server.city_list
TempFont = font.Font(window, size=20, weight='bold', family='온글잎 원슝')

# ====시/군 버튼 push====
# 시/군 검색 윈도우 open
def open_city_window():
    # === window 정리 ===
    clear_window()
    window.title("시/군 검색 기능")

    # === 시/군 검색어 입력 창 ===
    global city_search_text
    city_search_text = Text(window, height=1, width=30, font=TempFont)  # 세로 길이(height)를 조절
    city_search_text.pack(pady=60)

    # === 검색 버튼 - 일시적인 사용이므로 변수 제작하지 않음. ===
    Button(window, image=server.searchImage, bg="white", activebackground="dark grey", cursor="hand2", overrelief="sunken", command=search_city).place(x=525, y=57, width=40, height=40)

    # === 도시 목록 제공 ===
    Label(window, font= server.fontList,text="가평군, 고양시, 과천시, 광명시, 광주시, \
    구리시, 군포시, 김포시, 남양주시, 동두천시, \
    부천시, 성남시, 수원시, 시흥시, 안산시, \
    안성시, 안양시, 양주시, 양평군, 여주시, \
    연천군, 오산시, 용인시, 의왕시, 의정부시, \
    이천시, 파주시, 평택시, 포천시, 하남시, 화성시", wraplength=400).place(x=120, y=100)
# 시/군 검색어 입력 및 리스트 생성
def search_city():
    # === 검색어 입력 ===
    global city_search_text, city_search_term, city_searchListBox
    city_search_term = city_search_text.get("1.0", END).strip()

    # === 검색어[city_search_term] 기준으로 경기도 버스 정류소 현황 데이터 load ===
    # === 검색어[city_search_term] 기준으로 경기도 버스 정류소 현황 데이터 load ===
    url_busStation = 'https://openapi.gg.go.kr/BusStation?'
    params_busStation = {'KEY': server.gggokrKey, 'pSize': '1000', 'pIndex': '1', 'SIGUN_NM' : city_search_term}

    response = requests.get(url_busStation, params=params_busStation)
    root = ET.fromstring(response.text)
    this_city_stations = root.findall("row")

    # === [city_search_term] 기준으로 버스 정류소 리스트 생성 ===
    # === 스크롤바[city_Scrollbar] 및 리스트 박스[city_SearchListBox] 위치 지정 ===
    city_scrollbar = Scrollbar(window)
    city_scrollbar.place(x=560, y=250, width=20, height=500)

    city_searchListBox = Listbox(window, font=TempFont, activestyle='dotbox', relief='ridge', yscrollcommand=city_scrollbar.set)
    city_searchListBox.place(x=25, y=250, width=535, height=500)

    city_scrollbar.config(command=city_searchListBox.yview)

    # === 리스트 박스[city_SearchListBox] 원소 채우기 ===
    for i, item in enumerate(this_city_stations, start=1):
        str = city_search_term + " " + item.findtext("STATION_NM_INFO")
        city_searchListBox.insert(i + 1, str)

    # === 정류장 상세 정보 출력을 위한 함수로 이동하기 위함 ===
    # === 리스트 박스 내의 원소 클릭 setBusStation()으로 이동 ===

    # === 버튼 누르면 정류장 상세 정보 출력을 위해 준비하는 함수로 이동 [readyto_search_BusStation_fromCity]===
    Button(window, image=server.searchImage, bg="white", activebackground="dark grey",
           cursor="hand2", overrelief="sunken", command=readyto_search_busStation_fromCity).place(x=250, y=750)

def readyto_search_busStation_fromCity():
    global selectedCity, city_search_term, city_searchListBox, busStation_search_term
    selectedCity = city_search_term
    busStation_search_term = city_searchListBox.get(city_searchListBox.curselection())[4:]

    # 윈도우 정리하기
    clear_window()
    Label(window, font=server.fontList, text=busStation_search_term + " 정류장에 대한 정보입니다.").place(x=20, y=85, width=560, height=40)

    search_BusStation()

# ====정류장 버튼 push====
# 정류장 검색 윈도우 open
def open_busStation_window():
    # === window 정리 ===
    clear_window()
    window.title("정류소 검색 기능")

    # === 시/군 검색어 입력 창 ===
    global busStation_search_text, cityList_searchListBox
    busStation_search_text = Text(window, height=1, width=15, font=TempFont)
    busStation_search_text.place(x=305, y=165)

    # === [도시명] 기준으로 리스트 생성 ===
    # === 스크롤바 및 리스트 박스 위치 지정 ===
    cityList_scrollbar = Scrollbar(window)
    cityList_scrollbar.place(x=280, y=70, width=20, height=150)

    cityList_searchListBox = Listbox(window, font=TempFont, activestyle='dotbox', relief='ridge', yscrollcommand=cityList_scrollbar.set)
    cityList_searchListBox.place(x=25, y=70, width=255, height=150)

    cityList_scrollbar.config(command=cityList_searchListBox.yview)

    # === 리스트 원소 채우기 ===
    for i, s in enumerate(cityList):
        cityList_searchListBox.insert(i, s)

    # === 검색어 작성 유도 멘트 ===
    Label(window, font=server.fontList, text="정류장을 입력하세요.").place(x=305, y=85, width=275, height=40)
    # === 검색 버튼 - 일시적인 사용이므로 변수 제작하지 않음. ===
    Button(window, image=server.searchImage, bg="white", activebackground="dark grey",
                            cursor="hand2", overrelief="sunken", command=readyto_search_busStation).place(x=530, y=163, width=50, height=40)


def readyto_search_busStation():
    global selectedCity, cityList_searchListBox, busStation_search_text, busStation_search_term

    selectedCity = cityList_searchListBox.get(cityList_searchListBox.curselection())
    busStation_search_term = busStation_search_text.get("1.0", END).strip()

    print(selectedCity)
    search_BusStation()

# 정류장 검색어 입력 및 리스트 생성
def search_BusStation():
    # === 검색어 입력 ===
    global busStation_search_term
    print("검색어:", busStation_search_term)

    # === 검색어[도시명] 기준으로 경기도 버스 정류소 현황 데이터 load ===
    global selectedCity
    url_busStation = 'https://openapi.gg.go.kr/BusStation?'
    params_busStation = {'KEY': server.gggokrKey, 'pSize': '1000', 'pIndex': '1', 'SIGUN_NM': selectedCity}

    response = requests.get(url_busStation, params=params_busStation)
    root = ET.fromstring(response.text)
    items = root.findall("row")

    # === [도시명] 기준으로 받아온 데이터와 [정류장명]이 같은 경우의 [정류장ID] 받아오기 ===
    station_id = ""
    for i, item in enumerate(items, start=1):
        if busStation_search_term == item.findtext("STATION_NM_INFO"):
            station_id = item.findtext("STATION_ID")
            server.latitude = float(item.find("WGS84_LAT").text)
            server.longitude = float(item.find("WGS84_LOGT").text)
            server.station_name = busStation_search_term

    global busArrival_items
    # === 검색어[정류장ID] 기준으로 경기도 버스 도착 정보 조회 데이터 load  ===
    url_busArrival = 'http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalList?'
    params_busArrival = {'serviceKey': server.datagokrKey, 'stationId': station_id}

    busArrival_response = requests.get(url_busArrival, params=params_busArrival)
    busArrival_root = ET.fromstring(busArrival_response.text)
    busArrival_items = busArrival_root.findall(".//busArrivalList")

    # === [정류장ID] 기준으로 리스트 생성 ===
    # === 스크롤바 및 리스트 박스 위치 지정 ===
    busStation_scrollbar = Scrollbar(window)
    busStation_scrollbar.place(x=280, y=250, width=20, height=200)

    busStation_searchListBox = Listbox(window, font=TempFont, activestyle='dotbox', relief='ridge', yscrollcommand=busStation_scrollbar.set)
    busStation_searchListBox.place(x=25, y=250, width=255, height=200)

    busStation_scrollbar.config(command=busStation_searchListBox.yview)



    busStation_searchListBox.bind('<<ListboxSelect>>', setBus)
    # === 검색어 [루트ID] 기준으로 경기도 버스 노선 조회 데이터 load ===
    url_busRoute= 'http://apis.data.go.kr/6410000/busrouteservice/getBusRouteInfoItem'

    global busRoutes_items
    busRoutes_items = [busStation_search_term]
    # === 해당 [정류장ID]를 경유하는 [routeID]의 노선 번호 및 여러 데이터 출력하기 ===
    for i, item in enumerate(busArrival_items, start=1):
        print(item.findtext("routeId"))
        params_busRoute = {'serviceKey': server.datagokrKey, 'routeId': item.findtext("routeId")}
        busRoute_response = requests.get(url_busRoute, params=params_busRoute)
        busRoute_root = ET.fromstring(busRoute_response.text)
        busRoutes_items.append(busRoute_root.findall(".//busRouteInfoItem"))
        str = busRoutes_items[i][0].findtext("routeName") + "번 버스"
        busStation_searchListBox.insert(i, str)
# 도착 정보 출력
def show_BusStationInfo() :
    global index, busRoutes_items, busArrival_items
    str = busRoutes_items[index + 1][0].findtext("routeName") + "번 버스\n"
    if busArrival_items[index].findtext("predictTime1") != '':
        str += busArrival_items[index].findtext("predictTime1") + "분 후 도착 예정\n"
    if busArrival_items[index].findtext("predictTime2") != '':
        str += busArrival_items[index].findtext("predictTime2") + "분 후 도착 예정"
    arrivalLabel = Label(window, font=TempFont, text=str, wraplength=400)
    arrivalLabel.place(x=305, y=250, width=275, height=200)
    Button(window, image=server.searchImage, bg="white", activebackground="dark grey",
           cursor="hand2", overrelief="sunken", command=readyto_search_busRoute_fromStation).place(x=520, y=400, width=50, height=40)
    Button(window, image=server.searchImage, bg="white", activebackground="dark grey",
                            cursor="hand2", overrelief="sunken", command=map.onMapPopup).place(x=525, y=57, width=40, height=40)

# === 이벤트 발생 함수 ===
def setBus(event):                      # 정류장 선택 > 도시 선택 > 정류장명 작성 > 해당 정류장의 버스 목록 중 하나 선택 시 실행.
    tmp = event.widget.curselection()
    if tmp:
        global index
        index = event.widget.curselection()[0]
        show_BusStationInfo()


# ====버스 버튼 push - 승희====
# 버스 검색 윈도우 open
def open_bus_window() :
    # === window 정리 ===
    clear_window()
    window.title("버스 노선 검색 기능")

    # === 버스 노선 검색어 입력 창 ===
    global busRoute_search_text

    busRoute_search_text = Text(window, height=1, width=30, font=TempFont)  # 세로 길이(height)를 조절
    busRoute_search_text.pack(pady=80)

    Label(window, font=server.fontList, text="버스 노선 명을 입력하세요.").place(x=90, y=35, width=400, height=40)
    # === 검색 버튼 - 일시적인 사용이므로 변수 제작하지 않음. ===
    Button(window, image=server.searchImage, bg="white", activebackground="dark grey", cursor="hand2", overrelief="sunken", command=readyto_search_busRoute).place(x=525, y=77, width=40, height=40)

def readyto_search_busRoute():
    global busRoute_search_text, busRoute_search_term

    busRoute_search_term = busRoute_search_text.get("1.0", END).strip()

    search_bus()
def readyto_search_busRoute_fromStation():
    global busRoute_search_text, busRoute_search_term, index, busRoutes_items

    busRoute_search_term = busRoutes_items[index + 1][0].findtext("routeName")

    search_bus()
# 버스 검색어 입력 및 리스트 생성
def search_bus():
    global busRoute_search_term, busRoute_items
    print("검색어:", busRoute_search_term)

    # === [routeId]를 기준 ===
    url_busRoute = 'http://apis.data.go.kr/6410000/busrouteservice/getBusRouteList'
    params_busRoute = {
        'serviceKey': 'xmFs5IrPwwEJmSe8Pu6PcPO8P6+iVF5mfCz/yTZ3WPmUjST6KEDtbhXDh9hAil7MP4Mhgli8CiW91OzNPR5N+A==', \
        'keyword': busRoute_search_term}

    busRoute_response = requests.get(url_busRoute, params=params_busRoute)
    busRoute_root = ET.fromstring(busRoute_response.text)
    busRoute_items = busRoute_root.findall(".//busRouteList")

    # === [city_search_term] 기준으로 버스 정류소 리스트 생성 ===
    # === 스크롤바[city_Scrollbar] 및 리스트 박스[city_SearchListBox] 위치 지정 ===
    busRoute_scrollbar = Scrollbar(window)
    busRoute_scrollbar.place(x=560, y=150, width=20, height=250)

    busRoute_searchListBox = Listbox(window, font=TempFont, activestyle='dotbox', relief='ridge', yscrollcommand=busRoute_scrollbar.set)
    busRoute_searchListBox.place(x=25, y=150, width=535, height=250)

    busRoute_scrollbar.config(command=busRoute_searchListBox.yview)

    # === 리스트 박스[city_SearchListBox] 원소 채우기 ===
    for i, item in enumerate(busRoute_items, start=1):
        str = item.findtext("routeName") + " | " + item.findtext("regionName") + " | " +item.findtext("routeTypeName")
        busRoute_searchListBox.insert(i, str)

    busRoute_searchListBox.bind('<<ListboxSelect>>', show_busRouteInfo)

def show_busRouteInfo(event):
    global busRoute_items
    selectedBus = event.widget.curselection()[0]
    busRoute_notebook = tkinter.ttk.Notebook(window)
    busRoute_notebook.place(x=25, y=450, width=535, height=280)

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

# === functions ===
def InitScreen():  # 메인 GUI 창을 시작하는 함수
    global buttonSize
    buttonSize = 200

    # === frame arrangement ===
    # 분류 제목 레이블 부분
    global CityLabel, StationLabel, LineNumberLabel
    CityLabel = Label(window, text="시/군", font=server.fontLabel, bg="white", image=server.labelImage, compound='center')
    StationLabel = Label(window, text="정류소명", font=server.fontLabel, bg="white", image=server.labelImage, compound='center')
    LineNumberLabel = Label(window, text="노선명", font=server.fontLabel, bg="white", image=server.labelImage, compound='center')

    # 줄 맞추기 정보
    CityLabel.place(x=0, y=470, width=buttonSize, height=buttonSize)
    StationLabel.place(x=200, y=470, width=buttonSize, height=buttonSize)
    LineNumberLabel.place(x=400, y=470, width=buttonSize, height=buttonSize)

    # 로고 버튼 - git 주소 연결
    global LogoLabel
    LogoLable = Button(window, image=server.logoImage, bg="white", command=onLogo, relief="flat",
                       activebackground="dark grey", cursor="hand2", overrelief="groove")
    LogoLable.place(x=10, y=10, width=580, height=500)

    # 시/군 검색 버튼 - 시/군 검색 페이지로
    global LocalSearchButton
    LocalSearchButton = Button(window, image=server.searchImage, bg="white", activebackground="dark grey",
                            cursor="hand2", overrelief="sunken", command=open_city_window)
    LocalSearchButton.place(x=0, y=600, width=buttonSize, height=buttonSize)

    # 정류소 명 검색 버튼
    global StationSearchButton
    StationSearchButton = Button(window, image=server.searchImage, bg="white", activebackground="dark grey",
                               cursor="hand2", overrelief="sunken", command=open_busStation_window, font=TempFont)
    StationSearchButton.place(x=200, y=600, width=buttonSize, height=buttonSize)

    # 노선 명 검색 버튼
    global LineSearchButton
    LineSearchButton = Button(window, image=server.searchImage, bg="white", activebackground="dark grey",
                               cursor="hand2", overrelief="sunken", command=open_bus_window)
    LineSearchButton.place(x=400, y=600, width=buttonSize, height=buttonSize)













if __name__ == '__main__':
    print("main laucher runned\n")
    InitScreen()
    window.mainloop()
else:
    print("main launcher imported\n")