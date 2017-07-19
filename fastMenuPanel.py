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

        self.tagsNames = {}
        self.tag = 'styleFont'
        self.tagIndex = 0
        self.keyForDel = None

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

        for key in self.tagsNames:
            self.text.tag_delete(key)

        for key in self.tagsNames:
            print(key)
            self.text.tag_add(key, self.tagsNames[key][0], self.tagsNames[key][1])
            self.tagsNames[key][2] = Font(family=self.fontsVar.get(), size=self.sizeVar.get())
            if self.tagsNames[key][3]:
                self.tagsNames[key][2].config(weight='bold')
                print('if bold')

            if self.tagsNames[key][4]:
                self.tagsNames[key][2].config(slant='italic')
                print('if slant')

            if self.tagsNames[key][5]:
                self.tagsNames[key][2].config(underline=1)
                print('if underline')

            self.text.tag_config(key, font=self.tagsNames[key][2])

    def setTextArea(self, textArea):
        self.text = textArea
        self.text.config(font=Font(family='Times New Roman', size=12))
        self.text.pack(expand=YES, fill=BOTH)

    def __setFont(self, weight=None, slant=None, underline=0):
        ind1 = self.text.index(SEL_FIRST)
        ind2 = self.text.index(SEL_LAST)

        isWeight = False
        isSlant = False
        isUndeline = False
        isBreak = False

        for index in range(len(self.tagsNames)):
            print(self.text.tag_names())
            for val in self.text.tag_names():
                if val != 'sel' and val != 'text':
                    print(val)
                    ranges = self.text.tag_ranges(val)
                    for tagRange in range(0, len(ranges), 2):

                        indList1 = list(map(int, ind1.split('.')))
                        indList2 = list(map(int, ind2.split('.')))
                        rangeList1 = list(map(int, str(ranges[tagRange]).split('.')))
                        rangeList2 = list(map(int, str(ranges[tagRange+1]).split('.')))

                        print(indList1, indList2, rangeList1, rangeList2)

                        if indList1 == rangeList1 and indList2 == rangeList2:
                            self.__checkFormats(val, weight, slant, underline)
                            self.text.tag_config(val, font=self.tagsNames[val][2])
                            self.tagsNames[val] = [ind1, ind2, self.tagsNames[val][2],
                                                   self.tagsNames[val][3],
                                                   self.tagsNames[val][4],
                                                   self.tagsNames[val][5]]
                            isBreak = True
                            break

                        if indList2 >= rangeList1 and indList2 <= rangeList2 and indList1 < rangeList1:
                            print('indList2 >= rangeList1 and indList2 <= rangeList2 and indList1 < rangeList1')
                            self.text.tag_add(val, ind1, ranges[tagRange+1])
                            self.__setFormats(val, weight, slant, underline)
                            self.text.tag_config(val, font=self.tagsNames[val][2])
                            isBreak = True
                            break

                        if indList1 >= rangeList1 and indList1 <= rangeList2 and indList2 > rangeList2:
                            print('indList1 >= rangeList1 and indList1 <= rangeList2 and indList2 > rangeList2')
                            self.text.tag_add(val, ranges[tagRange], ind2)
                            self.__setFormats(val, weight, slant, underline)
                            self.text.tag_config(val, font=self.tagsNames[val][2])
                            isBreak = True
                            break

                        if indList1 > rangeList1 and indList2 < rangeList2:
                            print('indList1 > rangeList1 and indList2 < rangeList2')
                            self.text.tag_delete(val)
                            self.text.tag_add(val, ranges[tagRange], ind1)
                            self.__setFormats(val, weight, slant, underline)
                            self.text.tag_config(val, font=self.tagsNames[val][2])
                            ind1 = ind2
                            ind2 = ranges[tagRange+1]
                            break

                        if indList1 >= rangeList1 and indList1 <= rangeList2 and indList2 == rangeList2:
                            print('indList1 >= rangeList1 and indList1 <= rangeList2 and indList2 == rangeList2; val =>', val)
                            self.text.tag_delete(val)
                            self.text.tag_add(val, ranges[tagRange], ind1)
                            self.__forDeletedTags(val)
                            self.text.tag_config(val, font=self.tagsNames[val][2])
                            isBreak = True
                            break

                        if indList1 == rangeList1 and indList2 >= rangeList1 and indList2 <= rangeList2:
                            print('indList1 == rangeList1 and indList2 >= rangeList1 and indList2 <= rangeList2')
                            self.text.tag_add(val, ind2, ranges[tagRange+1])
                            self.__forDeletedTags(val)
                            self.text.tag_config(val, font=self.tagsNames[val][2])
                            isBreak = True
                            break

            if isBreak:
                break
        else:
            tag = self.tag + str(self.tagIndex)

            if weight is not None:
                font = Font(family=self.fontsVar.get(), size=self.sizeVar.get(), weight=weight)
                isWeight = True

            if slant is not None:
                font = Font(family=self.fontsVar.get(), size=self.sizeVar.get(), slant=slant)
                isSlant = True

            if underline:
                font = Font(family=self.fontsVar.get(), size=self.sizeVar.get(), underline=underline)
                isUndeline = True

            self.text.tag_add(tag, ind1, ind2)
            self.text.tag_config(tag, font=font)
            self.tagsNames[tag] = [ind1, ind2, font, isWeight, isSlant, isUndeline]
            self.tagIndex += 1
            print('new teg added; tag =>', tag)

        if self.keyForDel is not None:
            del self.tagsNames[self.keyForDel]
            self.keyForDel = None

    def __checkFormats(self, val, weight, slant, underline):
        if weight is not None and self.tagsNames[val][3]:
            self.tagsNames[val][2].config(weight='normal')
            self.tagsNames[val][3] = False
            print('weight if')
        elif weight is not None and not self.tagsNames[val][3]:
            self.tagsNames[val][2].config(weight=weight)
            self.tagsNames[val][3] = True
            print('weight elif')

        if slant is not None and self.tagsNames[val][4]:
            self.tagsNames[val][2].config(slant='roman')
            self.tagsNames[val][4] = False
            print('slant if')
        elif slant is not None and not self.tagsNames[val][4]:
            self.tagsNames[val][2].config(slant=slant)
            self.tagsNames[val][4] = True
            print('slant elif')

        if underline and self.tagsNames[val][5]:
            self.tagsNames[val][2].config(underline=0)
            self.tagsNames[val][5] = False
            print('underline if')
        elif underline and not self.tagsNames[val][5]:
            self.tagsNames[val][2].config(underline=underline)
            self.tagsNames[val][5] = True
            print('underline elif')

    def __setFormats(self, val, weight, slant, underline):
        if weight:
            self.tagsNames[val][2].config(weight=weight)
            self.tagsNames[val][3] = True
            print('__setFormats weight')

        if slant:
            self.tagsNames[val][2].config(slant=slant)
            self.tagsNames[val][4] = True
            print('__setFormats slant')

        if underline:
            self.tagsNames[val][2].config(underline=underline)
            self.tagsNames[val][5] = True
            print('__setFormats underline')

    def __forDeletedTags(self, val):
        if self.tagsNames[val][3]:
            self.tagsNames[val][2].config(weight='bold')

        if self.tagsNames[val][4]:
            self.tagsNames[val][2].config(slant='italic')

        if self.tagsNames[val][5]:
            self.tagsNames[val][2].config(underline=1)
