import tkinter as tk
import tkinter.messagebox
from Control import Control

class View:
    def __init__(self, control : Control.Control):
        self.control = control

        # Init Window
        self.root = tk.Tk()
        self.root.title(u"Header File Generator")
        self.root.geometry("600x800")
        self.table_frame = tk.Frame(self.root)

        # Config Table
        lb_symbol = tk.Label(self.table_frame, width = 20)
        lb_symbol["text"] = "Symbol"
        lb_symbol.grid(row = 0, column = 0)

        lb_description = tk.Label(self.table_frame, width = 40)
        lb_description["text"] = "Description"
        lb_description.grid(row = 0, column = 1)

        lb_enable = tk.Label(self.table_frame, width = 10)
        lb_enable["text"] = "Enable"
        lb_enable.grid(row = 0, column = 2)

        for i, config in enumerate(self.control.getConfigs()):
            self.e = tk.Entry(self.table_frame, width=20)
            self.e.insert(tk.END, config.symbol)
            self.e.grid(row= i + 1, column = 0)

            self.e = tk.Entry(self.table_frame, width=40)
            self.e.insert(tk.END, config.description)
            self.e.grid(row= i + 1, column = 1)

            bt_enable = tk.Button(self.table_frame, text="ON", width= 5)
            bt_enable["text"] = "ON" if config.enable else "OFF"
            bt_enable["command"] = lambda id = i, button = bt_enable : self.toggle_enable(id, button)
            bt_enable.grid(row = i + 1, column = 2)
        self.table_frame.pack()

        # Generator Button
        self.bt_generate = tk.Button(self.root)
        self.bt_generate["text"] = "Generate Header"
        self.bt_generate["command"] = self.generateHeader
        self.bt_generate.pack(side=tk.BOTTOM, anchor=tk.SE)

    def start(self):
        self.root.mainloop()

    def generateHeader(self):
        self.control.generateHeader()
        tk.messagebox.showinfo("Header Generator Info", "Generated:{0}".format(self.control.header_config.path))

    def update(self):
        pass

    def toggle_enable(self, id, button : tk.Button):
        config = self.control.getConfigs()[id]
        config.enable = not config.enable
        button["text"] = "ON" if config.enable else "OFF"