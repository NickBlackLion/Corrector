from tkinter import *


# Class that makes hints ans comments on right panel
class PackCanvas:
    def __init__(self, canvas, pointsArray, correctorsArray, hintsDict, categoryName, colorDict):
        self.canvas = canvas
        self.pointsArray = pointsArray
        self.correctorsArray = correctorsArray
        self.hintsDict = hintsDict
        self.categoryName = categoryName
        self.colorDict = colorDict

    # Method that adds comments and hints under each other
    def packCanvas(self, var, textArea):
        if var:
            self.__createPoints()
            self.__createShape(self.pointsArray[-1], self.categoryName, self.colorDict[self.categoryName])
            self.__searcher(var, textArea, self.categoryName, self.colorDict[self.categoryName])
        else:
            self.__searcher(var, textArea, self.categoryName, self.colorDict[self.categoryName])
            self.__unPackCanvas()

    def __unPackCanvas(self):
        for index in self.hintsDict:
            self.canvas.delete(self.hintsDict[index])

        del self.hintsDict[self.categoryName]

        self.pointsArray.clear()

        for x in range(len(self.hintsDict)):
            self.__createPoints()

        if len(self.pointsArray) > 0:
            for value, mapIndex in zip(self.pointsArray, self.hintsDict):
                self.__createShape(value, mapIndex, self.colorDict[mapIndex])

    def __createPoints(self):
        if len(self.pointsArray) == 0:
            tup = (2, 2, self.canvas.winfo_width() - 5, self.canvas.winfo_height() / 2)
            self.pointsArray.append(tup)
        else:
            li = list(self.pointsArray[-1])
            for (i, j) in enumerate(li, start=1):
                if i % 2 == 0:
                    li[i - 1] = j + self.canvas.winfo_height() / 2 + 5
                else:
                    li[i - 1] = j

            self.pointsArray.append(tuple(li))

    def __createShape(self, coordinate, categoryName, color):
        self.shape = self.canvas.create_rectangle(coordinate, fill=color)
        self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), self.pointsArray[-1][-1] + 5))
        self.hintsDict[categoryName] = self.shape

    def __searcher(self, var, textArea, categoryName=None, color=None):
        allRegex = []
        with open(categoryName.strip('\n') + '.txt', 'rb') as f:
            for x in f:
                decodeStr = x.decode('utf-8')
                allRegex.append(decodeStr.strip('\n\r'))

        print(allRegex)

        text = textArea.get('1.0', END)
        textRows = re.split('\n', text)

        if var and len(textRows) > 0:
            row = 1

            for oneTextRow in textRows:
                for reg in allRegex:
                    summ = 0
                    firstMatched = 0
                    lastMatched = 0

                    print(reg)

                    while summ <= len(oneTextRow):
                        matched = re.search(reg, oneTextRow[summ:], re.IGNORECASE)

                        if matched != None:
                            firstMatched = summ + matched.start()
                            lastMatched = summ + matched.end()

                            summ += int(matched.end())
                            textArea.tag_add(categoryName.strip('\n'), '{0}.{1}'.format(row, firstMatched),
                                             '{0}.{1}'.format(row, lastMatched))
                            textArea.tag_configure(categoryName.strip('\n'), background=color)
                            textArea.tag_raise("sel")

                        if not lastMatched or matched is None:
                            break

                row += 1
        else:
            textArea.tag_delete(categoryName.strip('\n'))
