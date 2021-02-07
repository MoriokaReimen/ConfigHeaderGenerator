import tkinter as tk
import tkinter.messagebox
from Control import Control

class View:
    def __init__(self, control : Control.Control):
        self.control = control

        # Init Window
        self.root = tk.Tk()
        self.root.title(u"Header File Generator")
        self.root.geometry("700x800")

        self.config_frame = tk.Frame(self.root)

        # Config Table
        lb_symbol = tk.Label(self.config_frame, width = 20)
        lb_symbol["text"] = "Symbol"
        lb_symbol.grid(row = 0, column = 0)

        lb_description = tk.Label(self.config_frame, width = 40)
        lb_description["text"] = "Detail"
        lb_description.grid(row = 0, column = 1)

        lb_enable = tk.Label(self.config_frame, width = 10)
        lb_enable["text"] = "Enable"
        lb_enable.grid(row = 0, column = 2)

        for i, config in enumerate(self.control.getConfigs()):
            symbol_entry = tk.Entry(self.config_frame, width=20)
            symbol_entry.insert(tk.END, config.symbol)
            symbol_entry.config(state = tk.DISABLED)
            symbol_entry.config(disabledforeground = "black", disabledbackground = "white")
            symbol_entry.grid(row= i + 1, column = 0)

            detail_entry = tk.Entry(self.config_frame, width=40)
            detail_entry.insert(tk.END, config.detail)
            detail_entry.config(state = tk.DISABLED)
            detail_entry.config(disabledforeground = "black", disabledbackground = "white")
            detail_entry.grid(row= i + 1, column = 1)

            bt_enable = tk.Button(self.config_frame, text="ON", width= 5)
            bt_enable["text"] = "ON" if config.enable else "OFF"
            color = "green" if config.enable else "red"
            bt_enable.config(bg=color, activebackground = color)
            bt_enable["command"] = lambda id = i, button = bt_enable : self.toggle_config_enable(id, button)
            bt_enable.grid(row = i + 1, column = 2)
        self.config_frame.pack(side=tk.TOP, anchor=tk.NW)


        self.value_config_frame = tk.Frame(self.root)

        # Config Table
        lb_symbol = tk.Label(self.value_config_frame, width = 20)
        lb_symbol["text"] = "Symbol"
        lb_symbol.grid(row = 0, column = 0)

        lb_description = tk.Label(self.value_config_frame, width = 40)
        lb_description["text"] = "Detail"
        lb_description.grid(row = 0, column = 1)

        lb_value = tk.Label(self.value_config_frame, width = 10)
        lb_value["text"] = "Value"
        lb_value.grid(row = 0, column = 2)

        lb_enable = tk.Label(self.value_config_frame, width = 10)
        lb_enable["text"] = "Enable"
        lb_enable.grid(row = 0, column = 3)

        for i, val_config in enumerate(self.control.getValConfigs()):
            symbol_entry = tk.Entry(self.value_config_frame, width=20)
            symbol_entry.insert(tk.END, val_config.symbol)
            symbol_entry.config(state = tk.DISABLED)
            symbol_entry.config(disabledforeground = "black", disabledbackground = "white")
            symbol_entry.grid(row= i + 1, column = 0)

            detail_entry = tk.Entry(self.value_config_frame, width=40)
            detail_entry.insert(tk.END, val_config.detail)
            detail_entry.config(state = tk.DISABLED)
            detail_entry.config(disabledforeground = "black", disabledbackground = "white")
            detail_entry.grid(row= i + 1, column = 1)

            value_entry = tk.Entry(self.value_config_frame, width=10)
            value_entry.insert(tk.END, val_config.value)
            value_entry.config(state = tk.DISABLED)
            value_entry.config(disabledforeground = "black", disabledbackground = "white")
            value_entry.grid(row= i + 1, column = 2)

            bt_enable = tk.Button(self.value_config_frame, text="ON", width= 5)
            bt_enable["text"] = "ON" if val_config.enable else "OFF"
            color = "green" if val_config.enable else "red"
            bt_enable.config(bg=color, activebackground = color)
            bt_enable["command"] = lambda id = i, button = bt_enable : self.toggle_val_config_enable(id, button)
            bt_enable.grid(row = i + 1, column = 3)
        self.value_config_frame.pack(side=tk.TOP, anchor=tk.W)

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

    def toggle_config_enable(self, id, button : tk.Button):
        config = self.control.getConfigs()[id]
        config.enable = not config.enable
        button["text"] = "ON" if config.enable else "OFF"
        color = "green" if config.enable else "red"
        button.config(bg=color, activebackground = color)
    
    def toggle_val_config_enable(self, id, button : tk.Button):
        val_config = self.control.getValConfigs()[id]
        val_config.enable = not val_config.enable
        button["text"] = "ON" if val_config.enable else "OFF"
        color = "green" if val_config.enable else "red"
        button.config(bg=color, activebackground = color)
