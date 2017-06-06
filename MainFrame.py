from tkinter import *


# Main window class
class MainFrame(Frame):
    # init method
    def __init__(self, master):
        Frame.__init__(self, master=master)
        self.pack()
        self.checkButtonsVarArray = []
        self.__checkButtonsFrame()
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
    def __checkButtonsFrame(self):
        checkFrame = Frame(self)
        checkFrame.config(bd=1, relief=SOLID)
        checkFrame.pack(side=RIGHT, anchor='n', padx=7, pady=7)

        with open('checkButtons') as f:
            for (index, word) in enumerate(f):
                var = IntVar()
                self.checkButtonsVarArray.append(var)
                Checkbutton(master=checkFrame, text=word.strip('\n'), variable=var).pack(anchor='w')

    # Get array with pressed buttons
    def getCheckButtonsArray(self):
        return self.checkButtonsVarArray
