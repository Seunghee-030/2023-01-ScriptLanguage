'''
server.py
모듈 간 데이터의 공유를 돕는 모듈입니다.
함수가 아닌 객체들로만 구성되어있습니다.
각 모듈에서 단순히 server를 import하면 필요한 정보를 제공받을 수 있습니다.
'''

# === inport ===
from tkinter import *
from tkinter import font

# === main window ===
window = Tk()
window.title("뻐스 - BBus")
window.geometry("600x800+450+200")
window.resizable(False, False)
window.configure(bg='white')

# === load image ===
searchImage = PhotoImage(file='image/search.png')  # search image
filterImage = PhotoImage(file='image/filter_icon.png')  # filter image
emailImage = PhotoImage(file='image/mail_icon3.png')  # mail image
mapImage = PhotoImage(file='image/map_icon2.png')  # map image
emptymarkImage = PhotoImage(file='image/white_bookmark.png')  # mark image
markImage = PhotoImage(file='image/bookmark.png')  # mark image
telegramImage = PhotoImage(file='image/telegram_icon.png')  # telegram image
logoImage = PhotoImage(file='image/뻐스.png')  # logo image
graphImage = PhotoImage(file='image/trend.png')  # graph image
noImage = PhotoImage(file='image/close.png')  # no image
labelImage = PhotoImage(file='image/label.png')  # label image
googleLinkImage = PhotoImage(file='image/google.png')  # label image
naverImage = PhotoImage(file='image/naver.png')  # label image
naverMapImage = PhotoImage(file='image/google_map.png')  # label image

# === load font ===
fontNormal = font.Font(window, size=14, family='G마켓 산스 TTF Medium')
fontLabel = font.Font(window, size=14, family='G마켓 산스 TTF Bold')
fontInfo = font.Font(window, size=10, family='G마켓 산스 TTF Medium')
fontList = font.Font(window, size=14, family='G마켓 산스 TTF Medium')

# === shared datas ===
info_text = None  # 노선 정보
route_name = None # 노선 이름
temp_window = None # 현재 윈도우
memo_text = None  # 메모
MarkDict_Station = dict()  # 북마크 dict {정류소명:정류소 정보}
MarkDict = dict()  # 북마크 dict {노선명 : 정보}

latitude = 0.0  # 위도
longitude = 0.0  # 경도

city_list = ['선택안함', '가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', \
             '김포시', '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', \
             '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시', '의정부시', \
             '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']

hList = [0 for i in city_list]

# 마우스 좌표 정보 (graph.py에서 사용)
mouse_x = 0
mouse_y = 0

if __name__ == '__main__':
    print("server.py runned\n")
else:
    print("server.py imported\n")