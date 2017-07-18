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

        self.fontStyleDict = {}
        self.fontStyleIndex = 0
        self.fonrStyleTag = 'fontStyleTag'

        OptionMenu(frame, self.fontsVar, *fontsList, command=lambda arg: self.__setFontToAllText()).pack(side=LEFT)
        OptionMenu(frame, self.sizeVar, *sizesList, command=lambda arg: self.__setFontToAllText()).pack(side=LEFT)

        Button(frame, text='B', font=Font(size='12', weight='bold'),
               command=lambda: self.__setFont(self.fontStyleDict, weight='bold')).pack(side=LEFT)

        Button(frame, text='I', font=Font(size='12', slant='italic'),
               command=lambda: self.__setFont(self.fontStyleDict, slant='italic')).pack(side=LEFT)

        Button(frame, text='U', font=Font(size='12', underline='1'),
               command=lambda: self.__setFont(self.fontStyleDict, underline=1)).pack(side=LEFT)

    def __setFontToAllText(self):
        self.text.tag_add('text', '1.0', END)
        self.font.config(family=self.fontsVar.get(), size=self.sizeVar.get())
        self.text.tag_config('text', font=self.font)

    def setTextArea(self, textArea):
        self.text = textArea
        self.text.config(font=Font(family='Times New Roman', size=12))
        self.text.pack(expand=YES, fill=BOTH)

    def __setFont(self, insDict, weight=None, slant=None, underline=0):
        ind1 = ''
        ind2 = ''

        try:
            ind1 = self.text.index(SEL_FIRST)
            ind2 = self.text.index(SEL_LAST)
        except:
            print(self.text.tag_names(INSERT))

        isUndeline = False
        isWeight = False
        isSlant = False

        for key in insDict:
            mapInd1 = list(map(int, ind1.split('.')))
            mapInd2 = list(map(int, ind2.split('.')))
            mapInsDict0 = list(map(int, insDict[key][0].split('.')))
            mapInsDict1 = list(map(int, insDict[key][1].split('.')))

            if mapInd1 == mapInsDict0 and mapInd2 == mapInsDict1:
                if weight is None and slant is None:
                    insDict[key][2].config(underline=underline)
                    isUndeline = insDict[key][5]
                elif slant is None and underline == 0:
                    insDict[key][2].config(weight=weight)
                    isWeight = insDict[key][3]
                elif weight is None and underline == 0:
                    insDict[key][2].config(slant=slant)
                    isSlant = insDict[key][4]

                if weight == 'bold' and insDict[key][3]:
                    insDict[key][2].config(weight='normal')
                    insDict[key][3] = False
                    print("weight == 'bold' and insDict[key][3]")
                elif weight == 'bold' and not insDict[key][3]:
                    insDict[key][2].config(weight='bold')
                    insDict[key][3] = True
                    print("weight == 'bold' and not insDict[key][3]")
                elif slant == 'italic' and insDict[key][4]:
                    insDict[key][2].config(slant='roman')
                    insDict[key][4] = False
                    print("slant == 'italic' and insDict[key][4]")
                elif slant == 'italic' and not insDict[key][4]:
                    insDict[key][2].config(slant='italic')
                    insDict[key][4] = True
                    print("slant == 'italic' and not insDict[key][4]")
                elif underline == 1 and insDict[key][5]:
                    insDict[key][2].config(underline=0)
                    insDict[key][5] = False
                    print("underline == 1 and insDict[key][5]")
                elif underline == 1 and not insDict[key][5]:
                    insDict[key][2].config(underline=1)
                    insDict[key][5] = True
                    print("underline == 1 and not insDict[key][5]")

                # insDict[key][2].config(weight='bold')
                self.text.tag_config(key, font=insDict[key][2])
                break
            elif mapInd1 > mapInsDict0 and mapInd2 == mapInsDict1:
                print('key =>', key, "mapInd1 > mapInsDict0 and mapInd2 == mapInsDict1")
                for keyIns in insDict:
                    ranges = self.text.tag_ranges(keyIns)
                    for i in range(0, len(ranges), 2):
                        start = ranges[i]
                        gotList = list(map(int, str(start).split('.')))
                        if gotList < mapInd2:
                            self.text.tag_delete(keyIns)

                if weight is None and slant is None:
                    isUndeline = True
                    insDict[key][2].config(underline=1)

                if slant is None and underline == 0:
                    isWeight = True
                    insDict[key][2].config(weight='bold')

                if weight is None and underline == 0:
                    isSlant = True
                    insDict[key][2].config(slant='italic')

                self.text.tag_add(key, insDict[key][0], ind1)
                self.text.tag_config(key, font=insDict[key][2])
                insDict[key] = [insDict[key][0], ind1, insDict[key][2], isWeight, isSlant, isUndeline]
                break
            elif mapInd1 == mapInsDict0 and mapInd2 < mapInsDict1:
                print('key =>', key, "mapInd1 == mapInsDict0 and mapInd2 < mapInsDict1")
                for keyIns in insDict:
                    ranges = self.text.tag_ranges(keyIns)
                    for i in range(0, len(ranges), 2):
                        start = ranges[i]
                        gotList = list(map(int, str(start).split('.')))
                        if gotList < mapInd2:
                            self.text.tag_delete(keyIns)

                if weight is None and slant is None:
                    isUndeline = True
                    insDict[key][2].config(underline=1)

                if slant is None and underline == 0:
                    isWeight = True
                    insDict[key][2].config(weight='bold')

                if weight is None and underline == 0:
                    isSlant = True
                    insDict[key][2].config(slant='italic')

                self.text.tag_add(key, ind2, insDict[key][1])
                self.text.tag_config(key, font=insDict[key][2])
                insDict[key] = [ind2, insDict[key][1], insDict[key][2], isWeight, isSlant, isUndeline]
                break
            elif mapInd2 == mapInsDict0:
                print('key =>', key, "mapInd2 == mapInsDict0")
                for keyIns in insDict:
                    ranges = self.text.tag_ranges(keyIns)
                    for i in range(0, len(ranges), 2):
                        start = ranges[i]
                        gotList = list(map(int, str(start).split('.')))
                        if gotList < mapInd2:
                            self.text.tag_delete(keyIns)

                if weight is None and slant is None:
                    isUndeline = True
                    insDict[key][2].config(underline=1)

                if slant is None and underline == 0:
                    isWeight = True
                    insDict[key][2].config(weight='bold')

                if weight is None and underline == 0:
                    isSlant = True
                    insDict[key][2].config(slant='italic')

                self.text.tag_add(key, ind1, insDict[key][1])
                self.text.tag_config(key, font=insDict[key][2])
                insDict[key] = [ind1, insDict[key][1], insDict[key][2], isWeight, isSlant, isUndeline]
                break
            elif mapInd1 == mapInsDict1:
                print('key =>', key, "mapInd1 == mapInsDict1")
                for keyIns in insDict:
                    ranges = self.text.tag_ranges(keyIns)
                    for i in range(0, len(ranges), 2):
                        start = ranges[i]
                        gotList = list(map(int, str(start).split('.')))
                        if gotList < mapInd2:
                            self.text.tag_delete(keyIns)

                if weight is None and slant is None:
                    isUndeline = True
                    insDict[key][2].config(underline=1)

                if slant is None and underline == 0:
                    isWeight = True
                    insDict[key][2].config(weight='bold')

                if weight is None and underline == 0:
                    isSlant = True
                    insDict[key][2].config(slant='italic')

                self.text.tag_add(key, insDict[key][0], ind2)
                self.text.tag_config(key, font=insDict[key][2])
                insDict[key] = [insDict[key][0], ind2, insDict[key][2], isWeight, isSlant, isUndeline]
                break
            elif mapInd1 == mapInsDict0 and mapInd2 > mapInsDict1:
                print('key =>', key, "mapInd1 == mapInsDict0 and mapInd2 > mapInsDict1")
                for keyIns in insDict:
                    ranges = self.text.tag_ranges(keyIns)
                    for i in range(0, len(ranges), 2):
                        start = ranges[i]
                        gotList = list(map(int, str(start).split('.')))
                        if gotList < mapInd2:
                            self.text.tag_delete(keyIns)

                if weight is None and slant is None:
                    isUndeline = True
                    insDict[key][2].config(underline=1)

                if slant is None and underline == 0:
                    isWeight = True
                    insDict[key][2].config(weight='bold')

                if weight is None and underline == 0:
                    isSlant = True
                    insDict[key][2].config(slant='italic')

                self.text.tag_add(key, ind1, ind2)
                self.text.tag_config(key, font=insDict[key][2])
                insDict[key] = [ind1, ind2, insDict[key][2], isWeight, isSlant, isUndeline]
                break
            elif mapInd1 < mapInsDict0 and mapInd2 == mapInsDict1:
                print('key =>', key, "mapInd1 < mapInsDict0 and mapInd2 == mapInsDict1")
                for keyIns in insDict:
                    ranges = self.text.tag_ranges(keyIns)
                    for i in range(0, len(ranges), 2):
                        start = ranges[i]
                        gotList = list(map(int, str(start).split('.')))
                        if gotList < mapInd2:
                            self.text.tag_delete(keyIns)

                if weight is None and slant is None:
                    isUndeline = True
                    insDict[key][2].config(underline=1)

                if slant is None and underline == 0:
                    isWeight = True
                    insDict[key][2].config(weight='bold')

                if weight is None and underline == 0:
                    isSlant = True
                    insDict[key][2].config(slant='italic')

                self.text.tag_add(key, ind1, ind2)
                self.text.tag_config(key, font=insDict[key][2])
                insDict[key] = [ind1, ind2, insDict[key][2], isWeight, isSlant, isUndeline]
                break
            elif mapInd1 > mapInsDict0 and mapInd2 < mapInsDict1:
                print('key =>', key, "mapInd1 > mapInsDict0 and mapInd2 < mapInsDict1")
                insIndex = insDict[key][1]
                self.text.tag_delete(key)
                self.text.tag_add(key, insDict[key][0], ind1)
                self.text.tag_config(key, font=insDict[key][2])
                insDict[key] = [insDict[key][0], ind1, insDict[key][2], isWeight, isSlant, isUndeline]

                ind1 = ind2
                ind2 = insIndex
        else:
            tag = self.fonrStyleTag + str(self.fontStyleIndex)

            if weight is None and slant is None:
                font = Font(family=self.fontsVar.get(), size=self.sizeVar.get(), underline=1)
                isUndeline = True

            if slant is None and underline == 0:
                font = Font(family=self.fontsVar.get(), size=self.sizeVar.get(), weight='bold')
                isWeight = True

            if weight is None and underline == 0:
                font = Font(family=self.fontsVar.get(), size=self.sizeVar.get(), slant='italic')
                isSlant = True

            print('in else for', 'tag =>', tag)
            self.text.tag_add(tag, ind1, ind2)
            self.text.tag_config(tag, font=font)
            insDict[tag] = [ind1, ind2, font, isWeight, isSlant, isUndeline]
            self.fontStyleIndex += 1
