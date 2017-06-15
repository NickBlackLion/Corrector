from tkinter import *
from searcher import *


# Class that makes hints ans comments on right panel
class PackCanvas:
    def __init__(self, canvas, pointsArray, correctorsArray, hintsDict, categoryName, colorDict):
        self.canvas = canvas
        self.pointsArray = pointsArray
        self.correctorsArray = correctorsArray
        self.hintsDict = hintsDict
        self.categoryName = categoryName
        self.colorDict = colorDict
        self.allRegex = []

    # Method that adds comments and hints under each other
    def packCanvas(self, var, textArea):
        if var:
            searcher(var, textArea, self.allRegex, self.__createHint, self.__deleteHint, self.categoryName, self.colorDict[self.categoryName])
        else:
            searcher(var, textArea, self.allRegex, self.__createHint, self.__deleteHint, self.categoryName, self.colorDict[self.categoryName])
            self.__deleteHint()
            self.allRegex.clear()

    def __createHint(self, event=None):
        if len(self.pointsArray) == 0:
            tup = (2, 2, self.canvas.winfo_width() - 5, self.canvas.winfo_height() - 5)

        self.shape = self.canvas.create_rectangle(tup, fill='white')
        self.hintsDict[self.categoryName] = self.shape

    def __deleteHint(self, event=None):
        for index in self.hintsDict:
            self.canvas.delete(self.hintsDict[index])

        self.pointsArray.clear()
