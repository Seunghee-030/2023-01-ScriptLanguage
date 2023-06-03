import tkinter as tk

# tkinter 창 생성
window = tk.Tk()
window.title("그래프 배치 예제")

# 캔버스 크기 설정
canvas_width = 450
canvas_height = 400

# Canvas 생성
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

# 그래프 그리기 함수
def draw_graph():
    bus_num = int(entry.get())  # 입력된 busNum 값 가져오기

    if bus_num < 1:
        bus_num = 1
    elif bus_num > 10:
        bus_num = 10

    graph_count = bus_num  # 그래프 개수
    max_graph_width = 50  # 그래프 최대 폭

    total_width = graph_count * max_graph_width
    start_x = (canvas_width - total_width) / 2  # 그래프 시작 x 좌표
    y_offset = 10  # 그래프 시작 y 좌표
    graph_width = min(max_graph_width, (canvas_width - (graph_count - 1) * max_graph_width) / graph_count)  # 그래프 폭

    for i in range(graph_count):
        x_offset = start_x + (graph_width + max_graph_width) * i  # 그래프의 x 위치

        canvas.create_rectangle(x_offset, y_offset, x_offset + graph_width, canvas_height - y_offset, fill="blue")

# 그래프 그리기 버튼 생성
button = tk.Button(window, text="그래프 그리기", command=draw_graph)
button.pack()

# busNum 입력 받을 Entry 생성
entry = tk.Entry(window)
entry.pack()

# tkinter 창 실행
window.mainloop()
