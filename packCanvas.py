from tkinter import *
from searcher import *


# Class that makes hints ans comments on right panel
class PackCanvas:
    def __init__(self, canvas, categoryName, color):
        self.categoryName = categoryName
        self.color = color
        self.canvas = canvas

        self.allRegex = {}
        self.createFoo = self.__createHint
        self.deleteFoo = self.__deleteHint
        self.hint = None

        self.shape = None
        self.text = None

    # Method that adds comments and hints under each other
    def packCanvas(self, var, textArea):
        if var:
            searcher(var, textArea, self)
        else:
            searcher(var, textArea, self)
            self.__deleteHint()
            self.allRegex.clear()

    def __createHint(self, event=None):
        tup = (2, 2, self.canvas.winfo_width() - 5, self.canvas.winfo_height() - 5)
        tup1 = (10, 5)

        self.shape = self.canvas.create_rectangle(tup, fill='white')
        self.text = self.canvas.create_text(tup1, anchor=NW, text=self.hint, width=self.canvas.winfo_width() - 5)

    def __deleteHint(self, event=None):
        if self.shape and self.text:
            self.canvas.delete(self.shape)
            self.canvas.delete(self.text)
