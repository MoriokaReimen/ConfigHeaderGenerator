import tkinter as tk
from Control import Control

class View:
    def __init__(self, control : Control.Control):
        self.control = control

        # Init Window
        self.root = tk.Tk()
        self.root.title(u"Header File Generator")
        self.root.geometry("600x800")

        # Config Table
        self.config_table = tk.Label(self.root)
        self.config_table["text"] = "Hello"
        self.config_table.pack(side=tk.TOP, anchor=tk.NW)

        # Generator Button
        self.bt_generate = tk.Button(self.root)
        self.bt_generate["text"] = "Generate Header"
        self.bt_generate.pack(side=tk.BOTTOM, anchor=tk.SE)

    def start(self):
        self.root.mainloop()

    def update(self):
        pass
