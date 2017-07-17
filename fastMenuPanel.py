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

        self.boldDict = {}
        self.boldIndex = 0
        self.boldTag = 'boldTag'

        self.slantDict = {}
        self.slantIndex = 0
        self.slantTag = 'slantTag'

        self.underlineDict = {}
        self.underlineIndex = 0
        self.underlineTag = 'underlineTag'

        self.selectedFont = Font(family=self.fontsVar.get(), size=self.sizeVar.get())

        OptionMenu(frame, self.fontsVar, *fontsList, command=lambda arg: self.__setFontToAllText()).pack(side=LEFT)
        OptionMenu(frame, self.sizeVar, *sizesList, command=lambda arg: self.__setFontToAllText()).pack(side=LEFT)

        Button(frame, text='B', font=Font(size='12', weight='bold'),
               command=lambda: self.__setFont(self.boldDict, weight='bold')).pack(side=LEFT)

        Button(frame, text='I', font=Font(size='12', slant='italic'),
               command=lambda: self.__setFont(self.slantDict, slant='italic')).pack(side=LEFT)

        Button(frame, text='U', font=Font(size='12', underline='1'),
               command=lambda: self.__setFont(self.underlineDict, underline=1)).pack(side=LEFT)

    def __setFontToAllText(self):
        self.text.tag_add('text', '1.0', END)
        self.font.config(family=self.fontsVar.get(), size=self.sizeVar.get())
        self.text.tag_config('text', font=self.font)

    def setTextArea(self, textArea):
        self.text = textArea
        self.text.pack(expand=YES, fill=BOTH)

    def __setFont(self, insDict, weight=None, slant=None, underline=0):
        ind1 = self.text.index(SEL_FIRST)
        ind2 = self.text.index(SEL_LAST)

        if weight is None and slant is None:
            self.selectedFont.config(underline=underline)

        if slant is None and underline == 0:
            self.selectedFont.config(weight=weight)

        if weight is None and underline == 0:
            self.selectedFont.config(slant=slant)

        insKey = None

        for key in insDict:
            if (ind1, ind2) == insDict[key]:
                if weight is None and slant is None:
                    self.selectedFont.config(underline=0)

                if slant is None and underline == 0:
                    self.selectedFont.config(weight='normal')

                if weight is None and underline == 0:
                    self.selectedFont.config(slant='italic')

                self.text.tag_config(key, font=self.selectedFont)
                insKey = key
                break
            elif ind1 > insDict[key][0] and ind2 == insDict[key][1]:
                print('ind1 > insDict[key][0] and ind2 == insDict[key][1]')
                print(key)
                self.text.tag_delete(key)
                self.text.tag_add(key, insDict[key][0], ind1)
                self.text.tag_config(key, font=self.selectedFont)
                insDict[key] = (insDict[key][0], ind1)
                break
            elif ind1 == insDict[key][0] and ind2 < insDict[key][1]:
                print('ind1 == insDict[key][0] and ind2 < insDict[key][1]')
                print(key)
                self.text.tag_delete(key)
                self.text.tag_add(key, ind2, insDict[key][1])
                self.text.tag_config(key, font=self.selectedFont)
                insDict[key] = (ind2, insDict[key][1])
                break
            elif ind2 == insDict[key][0]:
                print('ind2 == insDict[key][0]')
                print(key)
                self.text.tag_delete(key)
                self.text.tag_add(key, ind1, insDict[key][1])
                self.text.tag_config(key, font=self.selectedFont)
                insDict[key] = (ind1, insDict[key][1])
                break
            elif ind1 == insDict[key][1]:
                print('ind1 == insDict[key][1]')
                print(key)
                self.text.tag_delete(key)
                self.text.tag_add(key, insDict[key][0], ind2)
                self.text.tag_config(key, font=self.selectedFont)
                insDict[key] = (insDict[key][0], ind2)
                break
            elif ind1 == insDict[key][0] and ind2 > insDict[key][1]:
                print('ind1 == insDict[key][0] and ind2 > insDict[key]')
                print(key)
                self.text.tag_delete(key)
                self.text.tag_add(key, ind1, ind2)
                self.text.tag_config(key, font=self.selectedFont)
                insDict[key] = (ind1, ind2)
                break
            elif ind1 < insDict[key][0] and ind2 == insDict[key][1]:
                print('ind1 < insDict[key][0] and ind2 == insDict[key][1]')
                print(key)
                self.text.tag_delete(key)
                self.text.tag_add(key, ind1, ind2)
                self.text.tag_config(key, font=self.selectedFont)
                insDict[key] = (ind1, ind2)
                break
            elif ind1 > insDict[key][0] and ind2 < insDict[key][1]:
                print('ind1 > insDict[key][0] and ind2 < insDict[key][1]')
                print(key)
                indLast = insDict[key][1]
                self.text.tag_delete(key)
                self.text.tag_add(key, insDict[key][0], ind1)
                self.text.tag_config(key, font=self.selectedFont)
                insDict[key] = (insDict[key][0], ind1)
                print(insDict[key])

                tag = None
                if weight is None and slant is None:
                    tag = self.underlineTag + str(self.underlineIndex)

                if slant is None and underline == 0:
                    tag = self.boldTag + str(self.boldIndex)

                if weight is None and underline == 0:
                    tag = self.slantTag + str(self.slantIndex)

                self.text.tag_add(tag, ind2, indLast)
                self.text.tag_config(tag, font=self.selectedFont)
                insDict[tag] = (ind2, indLast)
                print(tag)

                if weight is None and slant is None:
                    self.underlineIndex += 1

                if slant is None and underline == 0:
                    self.boldIndex += 1

                if weight is None and underline == 0:
                    self.slantIndex += 1
                break
        else:
            tag = None
            if weight is None and slant is None:
                tag = self.underlineTag + str(self.underlineIndex)

            if slant is None and underline == 0:
                tag = self.boldTag + str(self.boldIndex)

            if weight is None and underline == 0:
                tag = self.slantTag + str(self.slantIndex)

            print('in else for', 'tag =>', tag)
            self.text.tag_add(tag, ind1, ind2)
            self.text.tag_config(tag, font=self.selectedFont)
            insDict[tag] = (ind1, ind2)

            if weight is None and slant is None:
                self.underlineIndex += 1

            if slant is None and underline == 0:
                self.boldIndex += 1

            if weight is None and underline == 0:
                self.slantIndex += 1

        if insKey is not None:
            print('in if insKey is not None')
            self.text.tag_delete(insKey)
            del insDict[insKey]
