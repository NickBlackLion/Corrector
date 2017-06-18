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
        self.textSizeChanged = False

        self.__isTextSizeChanged()

    def getTextArea(self):
        return self.textArea

    def setTextLength(self, textLength=0):
        self.textLength = textLength

    def clearTextArea(self):
        self.textArea.delete('1.0', END)
        self.textSizeChanged = False
        self.textLength = 0

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

        pointsArray = []
        colorDict = {}
        color = ['green', '#1283FF', '#AC8312', 'yellow', 'blue', 'red', 'brown']

        with open('categoryes', encoding='utf-8') as f:
            for (index, word) in enumerate(f):
                category = word.strip('\n')
                colorDict[category] = color[index]
                corrector = PackCanvas(canvas, pointsArray, category, colorDict)
                var = IntVar()
                Checkbutton(variable=var,
                            master=checkFrame,
                            text=category,
                            command=lambda x=var, y=corrector: y.packCanvas(x.get(), self.textArea)).pack(anchor='w')

    def __isTextSizeChanged(self):
        if len(self.textArea.get('1.0', END).strip('\n')) != self.textLength:
            self.textSizeChanged = True
        self.__job = self.after(500, self.__isTextSizeChanged)

    def isTextChanged(self):
        return self.textSizeChanged

    def resetTextSizeChanged(self):
        self.textSizeChanged = False
