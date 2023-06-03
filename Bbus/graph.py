'''
graph.py
런처에서 그래프 버튼을 누르면 실행되는 모듈입니다.

functions
- onGraphPopup
- drawGraph
- getData
- mouseClicked
- onMapPopup
- getStr
'''

# === import ===
from tkinter import *
from tkinter import font
import server

def drawGraph(busItems_toGraph, window):
    canvasWidth = 450
    canvasHeight = 400
    gap = 15

    graphCanvas = Canvas(width=canvasWidth, height=canvasHeight, bg='#000fa3')
    graphCanvas.place(x=40, y=210)

    standardFont = font.Font(graphCanvas, size=15, family='DungGeunMo')

    Label(window, text="[ SYSTEM ] :  정류장의 버스 현황입니다.", font=standardFont, bg='#000fa3', fg='white', anchor='w').place(x=40, y=150, width=450, height=60)

    busNum = len(busItems_toGraph)
    if busNum == 0:
        Label(graphCanvas, text="현재 운행 중인 버스가 없습니다.", font=standardFont, bg='#000fa3', fg='white', anchor='w').place(x=70, y=190)
        return

    # === 운행 중인 버스가 있는 경우 ===

    rectWidth = (canvasWidth - (gap*busNum) - 20) // busNum
    rectWidth = min(50, rectWidth)

    totalWidth = (gap*(busNum-1)) + (busNum * rectWidth)

    start_x = (canvasWidth//2)-(totalWidth//2)
    graph_height = canvasHeight-100

    for i in range(0, busNum):
        x1 = start_x + (rectWidth + gap) * i
        x2 = x1 + rectWidth
        graphCanvas.create_rectangle(x1, graph_height - i[1]*100, x2, graph_height, fill='white')
        Label(graphCanvas, text=i[0], font=standardFont, bg='#000fa3', fg='white', anchor='w', wraplength=10).place(x=x1+(rectWidth//3), y=graph_height+10)

if __name__ == '__main__':
    print("graph.py runned\n")
else:
    print("graph.py imported\n")