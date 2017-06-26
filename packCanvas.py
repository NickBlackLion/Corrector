from tkinter import *
from searcher import *


# Class that makes hints ans comments on right panel
class PackCanvas:
    def __init__(self, textArea, master, canvas, categoryName, color, packCanvases, shapes):
        self.categoryName = categoryName
        self.color = color
        self.canvas = canvas
        self.packCanvases = packCanvases
        self.packCanvases[categoryName] = self
        self.textArea = textArea

        self.allRegex = {}

        self.shapes = shapes
        self.searcher = Searcher(master, self.textArea, self)

    # Method that adds comments and hints under each other
    def packCanvas(self, var):
        if var:
            self.searcher.searcher(var)
        else:
            self.searcher.searcher(var)
            self.deleteHint()
            self.allRegex.clear()

    def createHint(self, event=None, reg=None):
        for key in self.packCanvases:
            self.packCanvases[key].deleteHint()

        tup = (2, 2, self.canvas.winfo_width() - 5, self.canvas.winfo_height() - 5)
        tup1 = (10, 5)

        shape = self.canvas.create_rectangle(tup, fill='white')
        text = self.canvas.create_text(tup1, anchor=NW, text=self.allRegex[reg], width=self.canvas.winfo_width() - 5)

        self.shapes.append(shape)
        self.shapes.append(text)

    def deleteHint(self, event=None):
        if len(self.shapes):
            for key in self.shapes:
                self.canvas.delete(key)
