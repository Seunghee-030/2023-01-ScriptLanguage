'''
book_mark.py
런처에서 북마크 버튼을 누르면 실행되는 모듈입니다.

functions
- onMarkPopup
- deleteHospital
- showInfo
- makeBookMark
'''

# === import ===
import pickle   # 피클 모듈을 사용한 북마크
from click import command
import server
import tkinter.messagebox as msgbox
import os
from tkinter import *
from tkinter import font
import tkinter.scrolledtext as st

# C/C++ 연동
try:
    import cLink
except:
    pass

selBus = None

# === functions ===
def onMarkPopup():  # 북마크 팝업을 띄움
    global popup
    print("BookMark button clicked")
    popup = Toplevel()
    popup.geometry("600x370")
    popup.title("북마크")
    popup.resizable(False, False)

    fontInfo = font.Font(popup, size=10, family='G마켓 산스 TTF Medium')
    fontList = font.Font(popup, size=14, family='G마켓 산스 TTF Medium')

    # 북마크 버스 목록 리스트박스
    global listBox
    ListScrollBar = Scrollbar(popup)
    listBox = Listbox(popup, selectmode='extended', font=fontList, width=10, height=15, \
        borderwidth=5, relief='ridge', yscrollcommand=ListScrollBar.set, cursor="hand2")

    dirpath = os.getcwd()
    if os.path.isfile(dirpath + '\mark'):
        f = open('mark', 'rb')
        dic = pickle.load(f)
        f.close()
        server.MarkDict = dic

    print(server.MarkDict.keys())
    i = 0
    for bus, info in server.MarkDict.items():
        print(bus)
        listBox.insert(i, bus)
        i = i + 1

    listBox.bind('<<ListboxSelect>>', showInfo)
    listBox.place(x = 10, y = 0, width=200, height=340)
    print("showInfo : ", showInfo)
    ListScrollBar.place(x = 200+10, y = 0, width=20, height=340)
    ListScrollBar.config(command=listBox.yview, cursor="sb_v_double_arrow")

    # 선택된 버스 정보 출력하는 ScrolledText
    global ST
    ST = st.ScrolledText(popup, font=fontInfo, cursor="arrow")
    ST.place(x = 390 + 20 - 185, y = 0, width=370, height=340)

    # 선택된 버스 삭제 버튼
    global deleteButton
    deleteButton = Button(popup, font=fontList, text='북마크에서 선택된 버스 제외하기', command=deleteBusBookmark)
    deleteButton.place(x = 0, y = 340, width=800-200, height=30)

def deleteBusBookmark():       # 북마크에서 선택된 버스을 삭제하는 함수
    global ST
    if len(server.MarkDict) == 0:   # 북마크가 빈 상태에서 삭제 버튼을 누른 경우
        msgbox.showinfo("알림", "북마크가 비어있습니다.")
        popup.focus_set()
    else:
        if selBus in server.MarkDict:
            del server.MarkDict[selBus]

            f = open('mark', 'wb')
            pickle.dump(server.MarkDict, f)
            f.close()
            ST.delete('1.0', END)

def showInfo(event):   # 버스 리스트박스에서 버스 선택 시 정보 출력하는 함수
    global InfoLabel, ST, selBus
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        selBus = data

        if data in server.MarkDict:
            info = server.MarkDict[data]
            ST.configure(state="normal")    # 수정 가능으로 풀어놨다가,
            ST.delete('1.0', END)
            ST.insert(INSERT, info)
            ST.configure(state="disabled")  # 수정 불가능(읽기 전용)으로 변경

def makeBookMark():
    # 북마크를 추가하는 함수
    if server.route_name:
        if server.route_name in server.MarkDict:
            msgbox.showinfo("알림", "이미 북마크에 추가한 버스입니다.")

        else:
            text = server.info_text + '\n\n' + '[MEMO]' + '\n' + server.memo_text

            dirpath = os.getcwd()

            if os.path.isfile(dirpath + '\mark'):
                f = open('mark', 'rb')
                server.MarkDict = pickle.load(f)
                f.close()

                server.MarkDict[server.route_name] = text

                f = open('mark', 'wb')
                pickle.dump(server.MarkDict, f)
                f.close()

                f = open('mark', 'rb')
                server.MarkDict = pickle.load(f)
                f.close()

                print(server.MarkDict)

            else:
                server.MarkDict[server.route_name] = text
                f = open('mark', 'wb')
                pickle.dump(server.MarkDict, f)
                f.close()

                print(server.MarkDict)

            # C/C++ 연동
            try:        # cLink.pyd 파일을 Lib에 추가시킨 경우
                text = "성공적으로 북마크를 저장했습니다.\n메모 글자수: " + str(cLink.strlen(server.memo_text)) + "자"
                msgbox.showinfo("알림", text)
            except:     # cLink.pyd 파일을 Lib에 추가시키지 않은 경우
                msgbox.showinfo("알림", "성공적으로 북마크를 저장했습니다.")

    else:   # 예외 처리
        msgbox.showinfo("알림", "목록에서 버스를 먼저 선택해주십시오.")


if __name__ == '__main__':
    print("book_mark.py runned\n")
else:
    print("book_mark.py imported\n")