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

if __name__ == '__main__':
    print("link.py runned\n")
else:
    print("link.py imported\n")