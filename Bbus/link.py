'''
link.py
링크 버튼을 누르면 실행되는 모듈입니다.
'''

# === import ===
import webbrowser
import server
import tkinter.messagebox as msgbox

# === functions ===
def onLogo():       # 로고 버튼을 누르면 해당 프로젝트의 깃허브로 연결
    url = 'https://github.com/Seunghee-030/2023-01-ScriptLanguage.git'
    webbrowser.open(url)

def onNaverLink():          # 네이버 로고 버튼을 누르면 해당 병원의 네이버 검색 결과로 연결
    if server.station_name:
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=' + server.station_name
        webbrowser.open(url)
    else:                   # 예외처리: 사용자가 병원을 선택하지 않고, 버튼을 누를 경우
        msgbox.showinfo("알림", "해당하는 정류소를 먼저 선택해주세요")

def onGoogleLink():         # 구글 로고 버튼을 누르면 해당 병원의 구글 검색 결과로 연결
    if server.station_name:
        url = 'https://www.google.com/search?q=' + server.station_name
        webbrowser.open(url)
    else:                   # 예외처리: 사용자가 병원을 선택하지 않고, 버튼을 누를 경우
        msgbox.showinfo("알림", "해당하는 정류소를 먼저 선택해주세요")

def onNaverMapLink():       # 네이버 지도 버튼을 누르면 해당 병원의 네이버 지도 검색 결과로 연결
    if server.station_name:
        url = 'https://map.naver.com/v5/search/' + server.station_name
        webbrowser.open(url)
    else:                   # 예외처리: 사용자가 병원을 선택하지 않고, 버튼을 누를 경우
        msgbox.showinfo("알림", "해당하는 정류소를 먼저 선택해주세요")

if __name__ == '__main__':
    print("link.py runned\n")
else:
    print("link.py imported\n")