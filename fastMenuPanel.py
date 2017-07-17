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

        self.selectedFont = Font(family=self.fontsVar.get(), size=self.sizeVar.get())

        OptionMenu(frame, self.fontsVar, *fontsList, command=lambda arg: self.__setFontToAllText()).pack(side=LEFT)
        OptionMenu(frame, self.sizeVar, *sizesList, command=lambda arg: self.__setFontToAllText()).pack(side=LEFT)

        Button(frame, text='B', font=Font(size='12', weight='bold'),
               command=lambda: self.__setBoldFont(self.boldDict)).pack(side=LEFT)

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

    def __setBoldFont(self, insDict):
        ind1 = self.text.index(SEL_FIRST)
        ind2 = self.text.index(SEL_LAST)

        insKey = None

        for key in insDict:
            if (ind1, ind2) == insDict[key]:
                self.text.tag_config(key, font=Font(family=self.fontsVar.get(),
                                                    size=self.sizeVar.get(), weight='normal'))
                insKey = key
                break
            elif ind1 > insDict[key][0] and ind2 == insDict[key][1]:
                print('ind1 > insDict[key][0] and ind2 == insDict[key][1]')
                self.text.tag_delete(key)
                self.text.tag_add(key, insDict[key][0], ind1)
                self.text.tag_config(key, font=Font(family=self.fontsVar.get(), size=self.sizeVar.get(), weight='bold'))
                insDict[key] = (insDict[key][0], ind1)
                break
            elif ind1 == insDict[key][0] and ind2 < insDict[key][1]:
                print('ind1 == insDict[key][0] and ind2 < insDict[key][1]')
                self.text.tag_delete(key)
                self.text.tag_add(key, ind2, insDict[key][1])
                self.text.tag_config(key, font=Font(family=self.fontsVar.get(), size=self.sizeVar.get(), weight='bold'))
                insDict[key] = (ind2, insDict[key][1])
                break
            elif ind2 == insDict[key][0]:
                print('ind2 == insDict[key][0]')
                self.text.tag_delete(key)
                self.text.tag_add(key, ind1, insDict[key][1])
                self.text.tag_config(key, font=Font(family=self.fontsVar.get(), size=self.sizeVar.get(), weight='bold'))
                insDict[key] = (ind1, insDict[key][1])
                break
            elif ind1 == insDict[key][1]:
                print('ind1 == insDict[key][1]')
                self.text.tag_delete(key)
                self.text.tag_add(key, insDict[key][0], ind2)
                self.text.tag_config(key, font=Font(family=self.fontsVar.get(), size=self.sizeVar.get(), weight='bold'))
                insDict[key] = (insDict[key][0], ind2)
                break
            elif ind1 == insDict[key][0] and ind2 > insDict[key][1]:
                print('ind1 == insDict[key][0] and ind2 > insDict[key]')
                self.text.tag_delete(key)
                self.text.tag_add(key, ind1, ind2)
                self.text.tag_config(key, font=Font(family=self.fontsVar.get(), size=self.sizeVar.get(), weight='bold'))
                insDict[key] = (ind1, ind2)
                break
            elif ind1 < insDict[key][0] and ind2 == insDict[key][1]:
                print('ind1 < insDict[key][0] and ind2 == insDict[key][1]')
                self.text.tag_delete(key)
                self.text.tag_add(key, ind1, ind2)
                self.text.tag_config(key, font=Font(family=self.fontsVar.get(), size=self.sizeVar.get(), weight='bold'))
                insDict[key] = (ind1, ind2)
                break
            elif ind1 > insDict[key][0] and ind2 < insDict[key][1]:
                print('ind1 > insDict[key][0] and ind2 < insDict[key][1]')
                indLast = insDict[key][1]
                self.text.tag_delete(key)
                self.text.tag_add(key, insDict[key][0], ind1)
                self.text.tag_config(key, font=Font(family=self.fontsVar.get(), size=self.sizeVar.get(), weight='bold'))
                insDict[key] = (insDict[key][0], ind1)
                print(insDict[key])

                tag = 'selected' + str(self.boldIndex)
                self.text.tag_add(tag, ind2, indLast)
                self.text.tag_config(tag, font=Font(family=self.fontsVar.get(), size=self.sizeVar.get(), weight='bold'))
                insDict[tag] = (ind2, indLast)
                print(insDict[tag])
                self.boldIndex += 1
                break
        else:
            tag = 'selected' + str(self.boldIndex)
            print('in else for')
            self.text.tag_add(tag, ind1, ind2)
            self.text.tag_config(tag, font=Font(family=self.fontsVar.get(), size=self.sizeVar.get(), weight='bold'))
            insDict[tag] = (ind1, ind2)
            self.boldIndex += 1

        if insKey is not None:
            print('in if insKey is not None')
            del insDict[insKey]
