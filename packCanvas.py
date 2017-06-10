from tkinter import *


# Class that makes hints ans comments on right panel
class PackCanvas:
    def __init__(self, canvas, pointsDict, indexes, correctorsArray):
        self.canvas = canvas
        self.pointsDict = pointsDict
        self.indexes = indexes
        self.correctorsArray = correctorsArray

    # Method that adds comments and hints under each other
    def packCanvas(self, var, textArea):
        self.searcher(var, textArea)

        if var:
            self.__createRect()
        else:
            self.__unPackCanvas()

        self.count = len(self.indexes)

        for x in self.correctorsArray:
            x.setCount(self.count)

    def __unPackCanvas(self):
        for index in self.pointsDict:
            self.canvas.delete(index)

        self.pointsDict.clear()
        self.indexes.clear()

        self.count -= 1

        if self.count > 0:
            for x in range(self.count):
                self.__createRect()

    def __createRect(self):
        if len(self.pointsDict) == 0:
            tup = (2, 2, self.canvas.winfo_width() - 5, self.canvas.winfo_height() / 2)
            self.shape = self.canvas.create_rectangle(tup, fill='white')
            self.pointsDict[self.shape] = tup
            self.indexes.append(self.shape)
        else:
            li = list(self.pointsDict[self.indexes[len(self.indexes) - 1]])
            for (i, j) in enumerate(li, start=1):
                if i % 2 == 0:
                    li[i-1] = j + self.canvas.winfo_height() / 2 + 5
                else:
                    li[i-1] = j

            self.shape = self.canvas.create_rectangle(tuple(li), fill='white')
            self.pointsDict[self.shape] = tuple(li)
            self.indexes.append(self.shape)
            self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), li[3] + 5))

    def setCount(self, count):
        self.count = count

    def searcher(self, checkVar, textArea):
        allRegex = []
        with open('data.txt') as f:
            for x in f:
                allRegex.append(x.strip('\n'))

        text = textArea.get('1.0', END)
        textRows = re.split('\n', text)

        if checkVar and len(textRows) > 0:
            row = 1

            for oneTextRow in textRows:
                for reg in allRegex:
                    print(oneTextRow)
                    print(reg)
                    summ = 0
                    firstMatched = 0
                    lastMatched = 0

                    while summ <= len(oneTextRow):
                        matched = re.search(reg, oneTextRow[summ:])

                        if matched != None:
                            firstMatched = summ + matched.start()
                            lastMatched = summ + matched.end()

                            summ += int(matched.end())
                            textArea.tag_add('start', '{0}.{1}'.format(row, firstMatched),
                                             '{0}.{1}'.format(row, lastMatched))
                            textArea.tag_configure('start', background='yellow')
                            textArea.tag_raise("sel")

                        if not lastMatched or matched is None:
                            break

                row += 1
        else:
            textArea.tag_delete('start')
