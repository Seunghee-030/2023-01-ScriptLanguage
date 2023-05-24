'''
BBus.py
프로그램의 메인모듈

functions
- InitScreen

'''

# === import ===
# from tkinter.tix import NoteBook
from turtle import bgcolor
from urllib.request import urlopen
from server import window
from tkinter import *
from tkinter import font
import tkinter.scrolledtext as st
from tkinter.ttk import Notebook, Style
from xml.etree import ElementTree

import server
from graph import *
from map import *
from telegram import *
from link import *
from book_mark import *

# === XML import ===
import requests #pip install requests
import xml.etree.ElementTree as ET
import tkinter

def open_new_window():
    pass

# 검색 기능창 띄우기
def SearchRoute():
    global tempPage
    tempPage = InitScreen()

    clear_window()
    field = '버스 노선'
    window.title(field + " 검색 기능창")
    window.geometry("600x800+450+200")
    window.resizable(False, False)
    window.configure(bg='white')

    # === 검색어 입력 창 ===
    global nameLabel
    nameLabel = Label(window, text="버스 노선 검색", font=server.fontLabel, bg="white", image=server.labelImage, compound='center')

    # 줄 맞추기 정보
    nameLabel.place(x=20, y=30, width=200, height=100)


    # === 검색어 입력 창 ===
    global rKeyword
    rKeyword = 0
    search_text = Text(window, height=1, width=22)  # 세로 길이(height)를 조절
    search_text.configure(font=("Helvetica", 27))  # 폰트 크기 조절
    search_text.place(x=50, y=105)

    # 검색 버튼 누를 시 seatch_term에 문자열 저장
    def perform_search():
        search_term = search_text.get("1.0", END).strip()
        print("search_term : ", search_term)
        global SearchListBox
        perform_search_route(search_term)
        server.route_name = search_term
        print("server.route_name",server.route_name)

    def perform_search_route(search_term):
        print("검색어:", search_term)
        # === List Box ===
        global SearchListBox
        ListBoxScrollbar = Scrollbar(window)
        ListBoxScrollbar.pack(fill='y', side='right')
        SearchListBox = Listbox(window, selectmode='extended', font="Helvetica", width=44, height=10, borderwidth=6,
                                relief='ridge', yscrollcommand=ListBoxScrollbar.set, cursor="hand2")
        SearchListBox.pack(side='left', fill='both')
        ListBoxScrollbar.config(command=SearchListBox.yview)

        # === 기본 정류소 목록 ===
        url_BusStation = 'http://apis.data.go.kr/6410000/busrouteservice/getBusRouteList'
        params_BusStation = {
            'serviceKey': 'xmFs5IrPwwEJmSe8Pu6PcPO8P6+iVF5mfCz/yTZ3WPmUjST6KEDtbhXDh9hAil7MP4Mhgli8CiW91OzNPR5N+A==', \
            'keyword': search_term}

        response = requests.get(url_BusStation, params=params_BusStation)
        root = ET.fromstring(response.text)
        items = root.findall(".//busRouteList")

        for item in items:
            nameNo = item.findtext("routeName")
            route_id = item.findtext("routeId")
            typeName = item.findtext("routeTypeName")

            data = [nameNo,route_id, typeName]
            for _ in enumerate(data):
                SearchListBox.insert(END, data)  # 리스트 삽입

        window.update()

        # === list box ===
        SearchListBox.pack()
        SearchListBox.bind('<<ListboxSelect>>', event_for_listbox)
        SearchListBox.place(x=50, y=200)
    # === 검색 버튼 ===
    search_button = Button(window, image=server.searchImage, bg="white", activebackground="dark grey",
                           cursor="hand2", overrelief="sunken", command=perform_search)
    search_button.place(x=500, y=100, width=50, height=50)


def event_for_listbox(event):  # command for list box
    # 북마크버튼 부분
    global MarkButton
    MarkButton = Button(window, image=server.emptymarkImage, bg="white", activebackground="dark grey", cursor="hand2",
                        overrelief="sunken", command=onMarkPopup)
    MarkButton.place(x=50, y=220+235, width=40, height=40)


    global InfoLabel, ST
    global searchKey
    searchKey = server.route_name
    print("diq : ", searchKey)
    selection = event.widget.curselection()
    if selection:  # 리스트 박스에서 클릭 발생 시
        index = selection[0]
        data = event.widget.get(index)
        # 노선 명(NO.)가 같으면...
        url_BusStation = 'http://apis.data.go.kr/6410000/busrouteservice/getBusRouteList'
        params_BusStation = { 'serviceKey': 'xmFs5IrPwwEJmSe8Pu6PcPO8P6+iVF5mfCz/yTZ3WPmUjST6KEDtbhXDh9hAil7MP4Mhgli8CiW91OzNPR5N+A==', \
                              'keyword': searchKey }
        response = requests.get(url_BusStation, params=params_BusStation)
        if response.text:
            print("...load clear...")
        root = ET.fromstring(response.text)
        items = root.findall(".//busRouteList")

        info = "null"
        #print("items = " , items)
        for item in items:  # 'row' element들
            #print("item = ", item)
            route_Name = item.findtext("routeName")
            route_TypeName = item.findtext("routeTypeName")
            datainfo = [route_Name, route_TypeName]
            tempList = item.find('routeId').text
            #print("tempList : ", tempList)

            # 클릭 했을 당시 해당하는 정보 저장
            if tempList == data[1]:
                info = '[노선번호]' + '\n' + getStr(item.find('routeName').text) + \
                           '\n\n' + '[노선아이디]' + '\n' + getStr(item.find('routeId').text) + \
                           '\n\n' + '[노선유형]' + '\n' + getStr(item.find('routeTypeCd').text) + \
                           '\n\n' + '[노선유형명]' + '\n' + getStr(item.find('routeTypeName').text) #+ \
                            #'\n\n' + '[기점정류소명]' + '\n' + getStr(item.find('startStationName')) + \
                           #'\n\n' + '[종점정류소명]' + '\n' + getStr(item.find('endStationName')) + \
                           #'\n\n' + '[평일 최소 배차시간]' + '\n' + getStr(item.find('peekAlloc')) + \
                           #'\n\n' + '[평일 최대 배차시간]' + '\n' + getStr(item.find('nPeekAlloc')) + \
                           #'\n\n' + '[운수업체명]' + '\n' + getStr(item.find('companyName')) + \
                          # '\n\n' + '[운수업체 전화번호]' + '\n' + getStr(item.find('companyTel'))
                server.route_name = getStr(item.find('routeName').text)

                    # 북마크 여부 표시
        if data in server.MarkDict:
            MarkButton.configure(image=server.markImage)
        else:
            MarkButton.configure(image=server.emptymarkImage)

        # 선택된 정보 서버로 넘기기
        server.info_text = info
        print(server.info_text)

        # 정보 부분 (notebook)
        global InfoLabel, ST, notebook
        style = Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background="gray")
        style.map("TNotebook", background=[("selected", "gray")])

        notebook = Notebook(window)
        notebook.place(x=50, y=500, width=500, height=280)

        # notebook page1: 노선 정보 출력
        ST = st.ScrolledText(window, font=server.fontInfo, cursor="arrow")
        notebook.add(ST, text="Info")

        # notebook page2: 메모
        global memoST
        frame3 = Frame(window, background='white', relief='flat', borderwidth=0)
        memoST = st.ScrolledText(frame3, relief='raised', font=server.fontInfo)
        memoST.place(x=0, y=0, width=380, height=288)
        memoButton = Button(frame3, text='북마크 저장', command=saveMemo, font=server.fontInfo, cursor="hand2")
        memoButton.place(x=0, y=288, width=380, height=30)

        # bookmark data load
        dirpath = os.getcwd()
        if os.path.isfile(dirpath + '\mark'):
            f = open('mark', 'rb')
            dic = pickle.load(f)  # 파일에서 리스트 load
            f.close()
            server.MarkDict = dic

        # 정보 출력
        ST.configure(state="normal")    # 수정 가능으로 풀어놨다가,
        ST.delete('1.0', END)
        ST.insert(INSERT, info)
        ST.configure(state="disabled")  # 수정 불가능(읽기 전용)으로 변경

    def update_info_text(self, info_text):
        self.info_label.configure(text=info_text)


def saveMemo():  # 메모를 저장해 서버로 넘기는 함수
        if server.route_name:
            server.memo_text = memoST.get("1.0", END)
            # print (server.memo_text)
            memoST.delete('1.0', END)
            makeBookMark()
        else:
            msgbox.showinfo("알림", "목록에서 버스을 먼저 선택해주십시오.")

# 화면 클리어 함수
widgets = []
tempPage = SearchRoute
def clear_window():

    global widgets
    widgets = []

    # 위젯 저장
    for widget in window.winfo_children():
        widgets.append(widget)

    # 현재 창에 있는 모든 위젯 제거
    for widget in window.winfo_children():
        widget.destroy()

    global tempPage
    print(type(SearchRoute))
    reset = Button(window, text="reset", bg="white", activebackground="dark grey", command=tempPage)
    reset.place(x=500, y=0, width=100, height=20)

    global home
    home = Button(window, text="home", bg="white", activebackground="dark grey", command=InitScreen)
    home.place(x=400, y=0, width=100, height=20)
# === functions ===
def InitScreen():  # 메인 GUI 창을 시작하는 함수
    clear_window()
    global buttonSize
    buttonSize = 200

    # === frame arrangement ===
    # 분류 제목 레이블 부분
    global CityLabel, StationLabel, LineNumerLabel
    CityLabel = Label(window, text="시/군", font=server.fontLabel, bg="white", image=server.labelImage, compound='center')
    StationLabel = Label(window, text="정류소명", font=server.fontLabel, bg="white", image=server.labelImage, compound='center')
    LineNumerLabel = Label(window, text="노선명", font=server.fontLabel, bg="white", image=server.labelImage, compound='center')

    # 줄 맞추기 정보
    CityLabel.place(x=0, y=470, width=buttonSize, height=buttonSize)
    StationLabel.place(x=200, y=470, width=buttonSize, height=buttonSize)
    LineNumerLabel.place(x=400, y=470, width=buttonSize, height=buttonSize)

    # 로고 버튼 - git 주소 연결
    global LogoLabel
    LogoLable = Button(window, image=server.logoImage, bg="white", command=onLogo, relief="flat",
                       activebackground="dark grey", cursor="hand2", overrelief="groove")

    LogoLable.place(x=10, y=10, width=580, height=500)

    # 시/군 검색 버튼 - 시/군 검색 페이지로
    global LocalSearchButton
    LocalSearchButton = Button(window, image=server.searchImage, bg="white", activebackground="dark grey",
                            cursor="hand2", overrelief="sunken", command=open_new_window)
    LocalSearchButton.place(x=0, y=600, width=buttonSize, height=buttonSize)

    # 정류소 명 검색 버튼
    global StationSearchButton
    StationSearchButton = Button(window, image=server.searchImage, bg="white", activebackground="dark grey",
                               cursor="hand2", overrelief="sunken", command=open_new_window)
    StationSearchButton.place(x=200, y=600, width=buttonSize, height=buttonSize)

    # 노선 명 검색 버튼
    global LineSearchButton
    LineSearchButton = Button(window, image=server.searchImage, bg="white", activebackground="dark grey",
                               cursor="hand2", overrelief="sunken", command=SearchRoute)
    LineSearchButton.place(x=400, y=600, width=buttonSize, height=buttonSize)


    button_clear = Button(window, text="Clear Window", command=clear_window)
    button_clear.place(x=0, y=0, width=buttonSize, height=buttonSize)
    button_clear.pack()


def getStr(s):  # utitlity function: 문자열 내용 있을 때만 사용
    return '정보없음' if not s else s


if __name__ == '__main__':
    print("main laucher runned\n")
    InitScreen()
    #SearchRoute()
    window.mainloop()
else:
    print("main launcher imported\n")

