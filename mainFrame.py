from createCanvas import *
from packCanvas import *

# Main window class
class MainFrame(Frame):
    # init method
    def __init__(self, master):
        Frame.__init__(self, master=master)
        self.pack()
        self.__rightPanelFrame()
        self.__makeMainTextFrame()

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
        checkFrame.pack(anchor='w', padx=7, pady=7)

        scrollCanvas.pack(side=RIGHT, expand=YES, fill=Y)
        canvas.pack(side=LEFT)

        correctorsArray = []
        pointsArray = {}

        for index in range(7):
            correctorsArray.append(PackCanvas(canvas, pointsArray))

        with open('checkButtons') as f:
            for (index, word) in enumerate(f):
                var = IntVar()
                Checkbutton(variable=var,
                            master=checkFrame,
                            text=word.strip('\n'),
                            command=lambda x=var, y=correctorsArray[index]: y.packCanvas(x.get())).pack(anchor='w')
