from CreateCanvas import *


# Main window class
class MainFrame(Frame):
    # init method
    def __init__(self, master):
        Frame.__init__(self, master=master)
        self.pack()
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
            for word in f:
                var = IntVar()
                Checkbutton(variable=var,
                            master=checkFrame,
                            text=word.strip('\n'),
                            command=lambda x=var: StopWord(self).packCanvas(x)).pack(anchor='w')


class StopWord:
    def __init__(self, master):
        self.canvas = Canvas(master=master, width=200, height=200, bg='white')

    def packCanvas(self, var):
        if var.get():
            self.canvas.pack(side=RIGHT)
        else:
            self.canvas.destroy()
