# -*- coding: utf-8 -*-
"""Tkinter widget class for displayin tasks
"""
import tkinter as tk
from .ScrollableFrame import *


class ConfigTable(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.control = control

        # add caption
        self.caption_frame = tk.Frame(self)
        self.caption_frame.pack(side=tk.TOP, anchor=tk.NW)

        # Symbol
        entry = tk.Label(
            self.caption_frame,
            text="Symbol",
            width=25,
            justify=tk.LEFT,
            anchor=tk.W,
            relief=tk.RIDGE,
            fg="white",
            bg="black")
        entry.grid(row=0, column=0)

        # Description
        entry = tk.Label(
            self.caption_frame,
            text="Description",
            width=25,
            justify=tk.LEFT,
            anchor=tk.W,
            relief=tk.RIDGE,
            fg="white",
            bg="black")
        entry.grid(row=0, column=1)

        # Show Entry
        self.task_table = VerticalScrolledFrame(self, height=700)
        self.task_table.pack(side=tk.TOP, anchor=tk.NW)

    def draw(self, tasks):
        self.flash()

        for j, config in enumerate(tasks):
            # Symbol
            entry = tk.Label(
                self.task_table.interior,
                text=config.symbol,
                width=25,
                justify=tk.LEFT,
                anchor=tk.W,
                relief=tk.RIDGE)
            entry.grid(row=j, column=0)

            # Description
            entry = tk.Label(
                self.task_table.interior,
                text=config.description,
                width=25,
                justify=tk.LEFT,
                anchor=tk.W,
                relief=tk.RIDGE)
            entry.grid(row=j, column=1)

    def flash(self):
        self.task_table.pack(side=tk.TOP, anchor=tk.NW, expand=True)
        # Clear table widgets
        for widget in self.task_table.interior.winfo_children():
            widget.destroy()

        # reset pack
        self.task_table.interior.pack_forget()
