from tkinter import *


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("Tkinter OOP Window")
        self.minsize(500, 400)
        self.wm_iconbitmap("myicon.ico")

        self.create_label()

    def create_label(self):
        label = Label(self, text="Tkinter Label Creation")
        label.config(
            font=('times', 40, 'bold')
        )
        label.grid(column=0, row=0)


window = Window()
window.mainloop()

