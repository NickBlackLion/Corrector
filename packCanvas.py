# Class that makes hints ans comments on right panel
class PackCanvas:
    def __init__(self, canvas, pointsDict, indexes, correctorsArray):
        self.canvas = canvas
        self.pointsDict = pointsDict
        self.indexes = indexes
        self.correctorsArray = correctorsArray

    # Method that adds comments and hints under each other
    def packCanvas(self, var):
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