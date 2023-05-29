import tkinter as tk
import PIL.Image, PIL.ImageTk, PIL.ImageSequence
def update_frame():
    try:
        # GIF 이미지 업데이트
        image.seek(image.tell() + 1)
    except EOFError:
        # 마지막 프레임에 도달한 경우 처음으로 되돌아감
        image.seek(0)

    # PhotoImage 객체 업데이트
    photo.paste(next(iterator))

    # 다음 프레임 업데이트 예약
    window.after(100, update_frame)  # 100ms마다 업데이트 (0.1초)
# Tkinter 창 생성
window = tk.Tk()

# GIF 이미지 로드
image = PIL.Image.open("image/춘식.gif")
iterator = PIL.ImageSequence.Iterator(image)
photo = PIL.ImageTk.PhotoImage(image)

# 이미지를 표시할 레이블 생성
label = tk.Label(window, image=photo)
label.pack()

update_frame()
# 창 실행
window.mainloop()
