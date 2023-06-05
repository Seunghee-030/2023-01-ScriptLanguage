'''
server.py
모듈 간 데이터의 공유를 돕는 모듈입니다.
함수가 아닌 객체들로만 구성되어있습니다.
각 모듈에서 단순히 server를 import하면 필요한 정보를 제공받을 수 있습니다.
'''

# === inport ===
from tkinter import *
from tkinter import font
from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk
import PIL.Image, PIL.ImageTk, PIL.ImageSequence


# === main window ===
window = Tk()
window.title("뻐스 - BBus")
window.geometry("1000x800+450+200")
window.resizable(False, False)

backGroundImage = PhotoImage(file='image/backGround.png')

Label(window,image=backGroundImage).place(x=0,y=0)

# === load image ===
url = "https://postfiles.pstatic.net/MjAyMzA1MjZfNzMg/MDAxNjg1MTA5MDYzMzEx.-M_kjwI2_MC0eiW305AxOgtcpjLHzAQFxlgSdI_L8lwg.pUbE2rR2nY3rQAR5DQ-APW11L0DMizGdcDnA3X2rRBog.GIF.elfgh29/main_image.gif?type=w773"
with urllib.request.urlopen(url) as u:
    raw_data = u.read()

im = Image.open(BytesIO(raw_data))

searchImage = PhotoImage(file='image/search_retro.png')  # search image
smallSearchImage = PhotoImage(file='image/smallSearch_retro.png')  # search
stationList = PhotoImage(file='image/stationList.png')  # search

filterImage = PhotoImage(file='image/filter_icon.png')  # filter image
emailImage = PhotoImage(file='image/mail_icon3.png')  # mail image
mapImage = PhotoImage(file='image/map.png')  # map image
emptymarkImage = PhotoImage(file='image/white_bookmark.png')  # mark image
markImage = PhotoImage(file='image/white_bookmark.png')  # mark image
telegramImage = PhotoImage(file='image/telegram_icon.png')  # telegram image

logo = PhotoImage(file='image/뻐스.png')  # logo image
logoImage = ImageTk.PhotoImage(im)  # logo image

# === GIF 이미지 로드 ===
gifImage = PIL.Image.open('image/main_image_gif.gif')
photo = PIL.ImageTk.PhotoImage(gifImage)
iterator = PIL.ImageSequence.Iterator(gifImage)
gifPhoto = PhotoImage(file= 'image/춘식.gif')

homeImage = PhotoImage(file='image/home.png')
homeIcon = PhotoImage(file='image/home_icon.png')
graphImage = PhotoImage(file='image/trend.png')  # graph image
noImage = PhotoImage(file='image/close.png')  # no image
labelImage = PhotoImage(file='image/label.png')  # label image
googleLinkImage = PhotoImage(file='image/google.png')  # label image
naverImage = PhotoImage(file='image/naver.png')  # label image
naverMapImage = PhotoImage(file='image/google_map.png')  # label image
busInfoImage = PhotoImage(file='image/busInfo_Image.png')  # label image
boomarkImage = PhotoImage(file='image/white_bookmark.png')  # label image

# === load font ===
fontNormal = font.Font(window, size=14, family='G마켓 산스 TTF Medium')
fontLabel = font.Font(window, size=14, family='G마켓 산스 TTF Bold')
fontInfo = font.Font(window, size=10, family='G마켓 산스 TTF Medium')
fontList = font.Font(window, size=14, family='G마켓 산스 TTF Medium')

# === shared datas ===
cityInfo = None
stationInfo = None
busInfo = None

isStation = False

info_text = None  # 정류소 정보
#hospital_name = None
station_name = None # 정류소 이름
memo_text = None  # 메모
MarkDict = dict()  # 북마크 dict {정류소명:정류소 정보}

latitude = 0.0  # 위도
longitude = 0.0  # 경도

city_list = ['가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', \
             '김포시', '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', \
             '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시', '의정부시', \
             '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']

hList = [0 for i in city_list]

# GIF 프레임 업데이트 함수
def update_frame():
    global gifImage, iterator
    try:
        gifImage.seek(gifImage.tell() + 1)      # GIF 이미지 업데이트
        photo.paste(next(iterator))     # PhotoImage 객체 업데이트

    except EOFError:      # 마지막 프레임에 도달한 경우 처음으로 되돌아감
        gifImage.seek(0)
        iterator = PIL.ImageSequence.Iterator(gifImage)

    #print("frame : ", gifImage.tell())

    # 다음 프레임 업데이트 예약
    window.after(150, update_frame)  # 150ms마다 업데이트 (0.15초)

# 인증키
gggokrKey = '10c9c010f1c84f0380fdbcd4c7e01cd7'
datagokrKey = 'djFNBIwaWVJkvgD56MeKPoMOwQXZfH7Xf7YsT2RWf5OcKHKeOh9vJzssSBS4FfZlPWSGtpOPWp7rEUFjILX4tg=='

# 마우스 좌표 정보 (graph.py에서 사용)
mouse_x = 0
mouse_y = 0

if __name__ == '__main__':
    print("server.py runned\n")
else:
    print("server.py imported\n")