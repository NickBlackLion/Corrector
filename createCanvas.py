from tkinter import *


class MakeCanvas:
    def __init__(self, master):
        self.canvas = Canvas(master=master, width=200, height=200)

    def draw(self):
        self.canvas.create_oval(10, 10, 20, 20)
