"""
    TKINTER

    Window: The window is the container where all other GUI elements live.

    Widgets: The elements through which users interact with the program; each widget is defined by a class.  Some of the
    more common widgets are:
        Label       Displays text on screen.
        Button      Can contain text and can perform an action when clicked.
        Entry       Text entry widget that allows only a single line of text; get(), delete(), insert()
        Text        Text entry that allows multiline text entry.
        Frame       A rectangular region used to group related widgets or proving padding between widgets.

"""
import tkinter as tk


class HelloWorldApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        self.greeting = tk.Label(           # Make a Text Widget.
            text="Hello, Tkinter",              # Assign text.
            foreground="blue",                  # Could be red, orange, yellow, green, purple, etc.
            background="#808080",               # Can also be hex values, however, must be a string (not 0xFFFFFF).
            width=20,                           # width in TEXT UNITS, or the width of a zero ("0") in default sys font.
            height=20)                          # height in TEXT UNITS, or the height of a zero in default sys font.
        self.greeting.pack()                    # Add Text Widget to the window (won't show otherwise)

        self.quit = tk.Button(              # Make a Button Widget.
            text="QUIT",
            foreground="white",
            background="red",
            command=self.master.destroy)        # Action when clicked.
        self.quit.pack(side="bottom")

        self.entry = tk.Entry(              # SMALL TEXT INPUT box, has:
            fg="yellow",                        # self.entry.get() to get text entered.
            bg="blue",                          # self.entry.delete(idx) or delete(start, end) to delete text in entry.
            width=50)                           # self.entry.insert(idx, text_to_insert) to insert text in entry.
        self.entry.pack()

        self.get_entry = tk.Button(
            text="get entry input",
            foreground="white",
            background="red",
            command=self.print_entry_input)
        self.get_entry.pack()

        self.text_box = tk.Text(

        )

    def create_widgets(self):
        self.hi_there = tk.Button()
        self.hi_there["text"] = "Hello world\n(clickme)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

    def print_entry_input(self):
        print(self.entry.get())

    def say_hi(self):
        print("hi there, everyone!")


window = tk.Tk()                                # Window contains all widgets (boxes, labels, buttons, etc.)
app = HelloWorldApplication(master=window)
app.mainloop()                                  # Tkinter EVENT LOOP; BLOCKING!






