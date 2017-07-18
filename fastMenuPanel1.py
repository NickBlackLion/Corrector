from tkinter import *
from tkinter.font import Font


class TopFastMenu:
    def __init__(self, master):
        frame = Frame(master=master)
        frame.pack(expand=YES, fill=X)

        fontsList = ['Times New Roman', 'Segoe UI', 'Arial']
        sizesList = [i+2 for i in range(30)]
        self.fontsVar = StringVar()
        self.fontsVar.set(fontsList[0])

        self.sizeVar = IntVar()
        self.sizeVar.set(sizesList[10])
        self.font = Font(family=self.fontsVar.get(), size=self.sizeVar.get())

        self.tagsNames = []
        self.tag = ''
        self.index = 0

        OptionMenu(frame, self.fontsVar, *fontsList, command=lambda arg: self.__setFontToAllText()).pack(side=LEFT)
        OptionMenu(frame, self.sizeVar, *sizesList, command=lambda arg: self.__setFontToAllText()).pack(side=LEFT)

        Button(frame, text='B', font=Font(size='12', weight='bold'),
               command=lambda: self.__setFont(weight='bold')).pack(side=LEFT)

        Button(frame, text='I', font=Font(size='12', slant='italic'),
               command=lambda: self.__setFont(slant='italic')).pack(side=LEFT)

        Button(frame, text='U', font=Font(size='12', underline='1'),
               command=lambda: self.__setFont(underline=1)).pack(side=LEFT)

    def __setFontToAllText(self):
        self.text.tag_add('text', '1.0', END)
        self.font.config(family=self.fontsVar.get(), size=self.sizeVar.get())
        self.text.tag_config('text', font=self.font)

    def setTextArea(self, textArea):
        self.text = textArea
        self.text.config(font=Font(family='Times New Roman', size=12))
        self.text.pack(expand=YES, fill=BOTH)

    def __setFont(self, weight=None, slant=None, underline=0):
        ind1 = ''
        ind2 = ''

        try:
            ind1 = self.text.index(SEL_FIRST)
            ind2 = self.text.index(SEL_LAST)
        except:
            print(self.text.tag_names(INSERT))

        if weight:
            ranges = self.text.tag_ranges
