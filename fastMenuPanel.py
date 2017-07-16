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
        self.selectedFont = Font(family=self.fontsVar.get(), size=self.sizeVar.get())

        OptionMenu(frame, self.fontsVar, *fontsList, command=lambda arg: self.__setFontToAllText()).pack(side=LEFT)
        OptionMenu(frame, self.sizeVar, *sizesList, command=lambda arg: self.__setFontToAllText()).pack(side=LEFT)

        Button(frame, text='B', font=Font(size='12', weight='bold'),
               command=lambda: self.__setBoldFont()).pack(side=LEFT)

        Button(frame, text='I', font=Font(size='12', slant='italic'),
               command=lambda: self.__setItalicFont()).pack(side=LEFT)

        Button(frame, text='U', font=Font(size='12', underline='1'),
               command=lambda: self.__setUndelineFont()).pack(side=LEFT)

    def __setFontToAllText(self):
        self.text.tag_add('text', '1.0', END)
        self.font.config(family=self.fontsVar.get(), size=self.sizeVar.get())
        self.text.tag_config('text', font=self.font)

    def setTextArea(self, textArea):
        self.text = textArea
        self.text.pack(expand=YES, fill=BOTH)

    def __setBoldFont(self):
        self.text.tag_add('selected', SEL_FIRST, SEL_LAST)
        self.selectedFont.config(weight='bold')
        self.text.tag_config('selected', font=self.selectedFont)

    def __setItalicFont(self):
        self.text.tag_add('selected', SEL_FIRST, SEL_LAST)
        self.selectedFont.config(slant='italic')
        self.text.tag_config('selected', font=self.selectedFont)

    def __setUndelineFont(self):
        self.text.tag_add('selected', SEL_FIRST, SEL_LAST)
        self.selectedFont.config(underline='1')
        self.text.tag_config('selected', font=self.selectedFont)
