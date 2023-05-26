from tkinter import Tk, Label, Frame

window = Tk()

frame = Frame(window)
frame.pack()

label1 = Label(frame, text="Label 1")
label1.pack()

label2 = Label(frame, text="Label 2")
label2.pack()

window.mainloop()