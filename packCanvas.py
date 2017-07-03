from tkinter import *
from searcher import *


# Class that makes hints ans comments on right panel
class PackCanvas:
    def __init__(self, textArea, master, categories, canvas, categoryName, color, packCanvases, shapes):
        self.categoryName = categoryName
        self.color = color
        self.canvas = canvas
        self.packCanvases = packCanvases
        self.packCanvases[categoryName] = self
        self.textArea = textArea
        self.categories = categories

        self.allRegex = {}
        self.replacements = {}

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
        tup1 = (35, 5)
        tup2 = (10, 5, 30, 16)

        line = ''
        sline = ''
        if self.categoryName == self.categories[len(self.categories) - 2]:
            sline = 'Запропонована заміна: '
            print(sline)
        elif self.categoryName == self.categories[len(self.categories) - 1]:
            sline = 'Синоніми: '
            print(sline)

        try:
            if self.allRegex[reg.lower()] != '\n':
                line = self.allRegex[reg.lower()]
                line += '\n' + sline + self.replacements[reg.lower()]
            else:
                line = sline + self.replacements[reg.lower()]
        except KeyError:
            line = self.allRegex[reg]

        shape = self.canvas.create_rectangle(tup, fill='white')
        square = self.canvas.create_rectangle(tup2, fill=self.color)
        text = self.canvas.create_text(tup1, anchor=NW, text=line, width=self.canvas.winfo_width() - 40)

        self.shapes.append(shape)
        self.shapes.append(text)
        self.shapes.append(square)

    def deleteHint(self, event=None):
        if len(self.shapes):
            for key in self.shapes:
                self.canvas.delete(key)
