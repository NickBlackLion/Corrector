# Class that makes hints ans comments on right panel
class PackCanvas:
    def __init__(self, canvas, pointsDict):
        self.canvas = canvas
        self.pointsDict = pointsDict
        self.canvas.config(scrollregion=(0, 0, 300, 1000))

    # Method that adds comments and hints under each other
    def packCanvas(self, var):
        if var:
            if len(self.pointsDict) == 0:
                tup = (2, 2, self.canvas.winfo_width() - 5, self.canvas.winfo_height() / 2)
                self.shape = self.canvas.create_rectangle(tup, fill='white')
                self.pointsDict[self.shape] = tup
            else:
                li = None
                for index in self.pointsDict:
                    li = list(self.pointsDict[index])
                    for (i, j) in enumerate(li, start=1):
                        if i % 2 == 0:
                            li[i-1] = j + self.canvas.winfo_height() / 2 + 5
                        else:
                            li[i-1] = j

                    self.shape = self.canvas.create_rectangle(tuple(li), fill='white')

                self.pointsDict[self.shape] = tuple(li)

            print(self.pointsDict)
        else:
            del self.pointsDict[self.shape]
            self.canvas.delete(self.shape)
            print(self.pointsDict)
