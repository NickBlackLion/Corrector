from tkinter import *
from searcher import *


# Class that makes hints ans comments on right panel
class PackCanvas:
    def __init__(self, textArea, master, canvas, categoryName, color, packCanvases):
        self.categoryName = categoryName
        self.color = color
        self.canvas = canvas
        self.packCanvases = packCanvases
        self.packCanvases[categoryName] = self
        self.textArea = textArea

        self.allRegex = {}
        self.createFoo = self.__createHint
        self.deleteFoo = self.deleteHint
        self.hint = None

        self.shape = None
        self.text = None
        self.master = master
        self.searcher = Searcher(self.master, self.textArea, self)

    # Method that adds comments and hints under each other
    def packCanvas(self, var):
        if var:
            self.searcher.searcher(var)
        else:
            self.searcher.searcher(var)
            self.deleteHint()
            self.allRegex.clear()

    def __createHint(self, event=None):
        for key in self.packCanvases:
            self.packCanvases[key].deleteHint()

        tup = (2, 2, self.canvas.winfo_width() - 5, self.canvas.winfo_height() - 5)
        tup1 = (10, 5)

        self.shape = self.canvas.create_rectangle(tup, fill='white')
        self.text = self.canvas.create_text(tup1, anchor=NW, text=self.hint, width=self.canvas.winfo_width() - 5)

    def deleteHint(self, event=None):
        if self.shape and self.text:
            self.canvas.delete(self.shape)
            self.canvas.delete(self.text)
