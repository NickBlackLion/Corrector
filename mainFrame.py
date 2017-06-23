from packCanvas import *
import re


# Main window class
class MainFrame(Frame):
    # init method
    def __init__(self, master):
        Frame.__init__(self, master=master)

        self.master = master
        self.textLength = 0
        self.__job = None
        self.textSizeChanged = False
        self.categories = []
        self.makeBackArray = []

        self.pack(expand=YES, fill=BOTH)
        self.__makeMainTextFrame()
        self.__rightPanelFrame()
        self.__isTextSizeChanged()

    def getTextArea(self):
        return self.textArea

    def setTextLength(self, textLength=0):
        self.textLength += textLength

    def resetTextLength(self):
        self.textLength = 0

    def clearTextArea(self):
        self.textArea.delete('1.0', END)
        self.textSizeChanged = False
        self.textLength = 0

    # Main text area creating method
    def __makeMainTextFrame(self):
        textFrame = Frame(master=self)
        textFrame.pack(side=LEFT, expand=YES, fill=BOTH)

        self.textArea = Text(master=textFrame)
        scrollbar = Scrollbar(master=textFrame)
        self.textArea.bind('<Key>', self.pressed)

        self.textArea.config(selectbackground='green', yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.textArea.yview)

        scrollbar.pack(side=RIGHT, fill=Y, expand=YES)
        self.textArea.pack(side=LEFT, expand=YES, fill=BOTH)

    # Frame with check buttons
    def __rightPanelFrame(self):
        commonFrame = Frame(self)
        checkFrame = Frame(commonFrame)

        checkFrame.config(bd=1, relief=SOLID)
        checkFrame.pack(anchor='w', padx=7, pady=7, expand=YES, fill=BOTH)
        canvas = Canvas(master=commonFrame)
        canvas.pack()

        commonFrame.pack(side=RIGHT, anchor='n')

        color = ['green', '#1283FF', '#AC8312', 'yellow', 'blue', 'red', 'brown']
        packCanvases = {}
        shapes = []

        with open('categoryes', encoding='utf-8') as f:
            for (index, word) in enumerate(f):
                category = word.strip('\n')
                self.categories.append(category)
                var = IntVar()
                corrector = PackCanvas(self.textArea, self.master, canvas, category, color[index], packCanvases, shapes)
                Checkbutton(variable=var,
                            master=checkFrame,
                            text=category,
                            command=lambda x=var, y=corrector: y.packCanvas(x.get())).pack(anchor='w')

    def __isTextSizeChanged(self):
        if len(self.textArea.get('1.0', END).strip('\n')) != self.textLength:
            self.textSizeChanged = True
        self.__job = self.after(500, self.__isTextSizeChanged)

    def isTextChanged(self):
        return self.textSizeChanged

    def resetTextSizeChanged(self):
        self.textSizeChanged = False

    def getCategories(self):
        return self.categories

    def getMackBackArray(self):
        return self.makeBackArray

    def pressed(self, event=None):
        matched = re.match('space|BackSpace|Return', event.keysym)

        if event.keysym.isalpha():
            if matched is not None or len(event.keysym) == 1:
                self.makeBackArray.append(self.textArea.get('1.0', END))
                if len(self.makeBackArray) > 30:
                    self.makeBackArray = self.makeBackArray[len(self.makeBackArray)-10:len(self.makeBackArray)]
