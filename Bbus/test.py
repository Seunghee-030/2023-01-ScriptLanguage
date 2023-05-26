from tkinter import Tk, Label
from PIL import Image, ImageTk

# Tkinter 윈도우 생성
window = Tk()

# 이미지 로드
image = Image.open("image/logo.png")
photo = ImageTk.PhotoImage(image)

# 레이블 위젯 생성 및 이미지 설정
label = Label(window, image=photo)
label.pack()

# 윈도우 실행
window.mainloop()