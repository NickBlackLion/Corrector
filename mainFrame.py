from tkinter import *
from packCanvas import *


# Main window class
class MainFrame(Frame):
    # init method
    def __init__(self, master):
        Frame.__init__(self, master=master)
        self.pack()
        self.__rightPanelFrame()
        self.__makeMainTextFrame()

        self.textLength = 0
        self.__job = None
        self.setTextLength()

    def getTextArea(self):
        return self.textArea

    def setTextLength(self, textLength=0):
        if self.__job is None:
            self.__resetCheckTextLength(textLength)
        else:
            self.after_cancel(self.__job)
            self.__resetCheckTextLength(textLength)

    def clearTextArea(self):
        self.textArea.delete('1.0', END)
        self.setTextLength()

    # Main text area creating method
    def __makeMainTextFrame(self):
        textFrame = Frame(master=self)
        textFrame.pack(side=LEFT)

        self.textArea = Text(master=textFrame)
        scrollbar = Scrollbar(master=textFrame)

        self.textArea.config(selectbackground='green', yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.textArea.yview)

        scrollbar.pack(side=RIGHT, fill=Y, expand=YES)
        self.textArea.pack(side=LEFT)

    # Frame with check buttons
    def __rightPanelFrame(self):
        commonFrame = Frame(self)
        checkFrame = Frame(commonFrame)

        canvas = Canvas(master=commonFrame)
        scrollCanvas = Scrollbar(master=commonFrame)
        canvas.config(yscrollcommand=scrollCanvas.set)
        scrollCanvas.config(command=canvas.yview)

        commonFrame.pack(side=RIGHT, anchor='n')

        checkFrame.config(bd=1, relief=SOLID)
        checkFrame.pack(anchor='w', padx=7, pady=7, expand=YES, fill=BOTH)

        scrollCanvas.pack(side=RIGHT, expand=YES, fill=Y)
        canvas.pack(side=LEFT)

        correctorsArray = []
        pointsDict = {}
        indexes = []

        with open('checkButtons') as f:
            for (index, word) in enumerate(f):
                correctorsArray.append(PackCanvas(canvas, pointsDict, indexes, correctorsArray))
                var = IntVar()
                Checkbutton(variable=var,
                            master=checkFrame,
                            text=word.strip('\n'),
                            command=lambda x=var, y=correctorsArray[index]: y.packCanvas(x.get(), self.textArea)).pack(anchor='w')

    def __isTextSizeChanged(self):
        if len(self.textArea.get('1.0', END).strip('\n')) != self.textLength:
            self.isTextSizeChanged = True
        self.__job = self.after(500, self.__isTextSizeChanged)
        return self.isTextSizeChanged

    def __resetCheckTextLength(self, textLength):
        self.isTextSizeChanged = False
        self.textLength = textLength
        self.__isTextSizeChanged()
