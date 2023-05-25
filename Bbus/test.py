import tkinter as tk

def get_selected_index():
    index = citySearchListBox.curselection()
    print(index)

root = tk.Tk()
citySearchListBox = tk.Listbox(root)
citySearchListBox.pack()

button = tk.Button(root, text="Get Selected Index", command=get_selected_index)
button.pack()

root.mainloop()