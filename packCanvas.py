# Class that makes hints ans comments on right panel
class PackCanvas:
    def __init__(self, canvas, pointsArray):
        self.canvas = canvas
        self.pointsArray = pointsArray

    # Method that adds comments and hints under each other
    def packCanvas(self, var):
        if var:
            if len(self.pointsArray) == 0:
                self.pointsArray.append((2, 2, self.canvas.winfo_width() - 5, self.canvas.winfo_height() / 2))
            else:
                lastTup = self.pointsArray[len(self.pointsArray) - 1]

                merge = []
                for (index, value) in enumerate(lastTup, start=1):
                    if index % 2 == 0:
                        merge.append(value + self.canvas.winfo_height()/2 + 5)
                    else:
                        merge.append(value)

                self.pointsArray.append(tuple(merge))

            self.lastIndex = len(self.pointsArray) - 1

            self.shape = self.canvas.create_rectangle(self.pointsArray[self.lastIndex], fill='white')
            self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(),
                                             self.canvas.winfo_height() / 2 + self.pointsArray[self.lastIndex][3]))
        else:
            self.canvas.delete(self.shape)
            self.pointsArray.remove(self.pointsArray[len(self.pointsArray)-1])
