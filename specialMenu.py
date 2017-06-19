from tkinter import *
import shelve


class SpecialMenu:
    def __init__(self, root, mainMenu, mainFrame):
        labels = ['Добавить стоп-слово',
                  'Добавить повторяемое слово',
                  'Добавить устоявшиеся выражения и русизмы',
                  'Добавить чередования',
                  'Добавить синонимы']

        self.specialMenu = Menu(mainMenu, tearoff=0)
        for value in labels:
            self.specialMenu.add_command(label=value, command=lambda lab=value: self.__makeCommonWindow(lab))
        mainMenu.add_cascade(label='Специальные функции', menu=self.specialMenu)

        self.root = root

        self.vowels = '[аеєиіїоуюя]'
        self.consonants = '[бвгґджзйклмнпрстфхцчшщ]'
        self.voicelessConsonants = '[пхктшчсц]'
        self.space = '\\s'
        self.otherLetters = '\\w+'
        self.double = '{2}'
        self.either = '|'

        self.frameConf = {'relief': SOLID, 'bd': 1}
        self.padConf = {'padx': 5, 'pady': 5, 'expand': YES, 'fill': BOTH}

    def __makeCommonWindow(self, label):
        top = Toplevel(master=self.root)
        top.title(label)

        self.__makeHelpButtons(top)
        self.__makeEntryFrame(top)
        self.__makeOkCancelButton(top)

    def __makeEntryFrame(self, master):
        areaSize = {'width': 70, 'height': 10}

        entryFrame = Frame(master)
        entryFrame.pack(self.padConf)

        Label(entryFrame, text='Шаблон поиска').pack()
        self.text = Text(entryFrame, areaSize)
        self.text.pack(expand=YES, fill=X)

        Label(entryFrame, text='Комментарий').pack()
        self.hint = Text(entryFrame, areaSize)
        self.hint.pack(expand=YES, fill=X)

    def __makeOkCancelButton(self, master):
        okCancelButtonFrame = Frame(master)
        okCancelButtonFrame.pack(self.padConf)

        Button(okCancelButtonFrame, text='Ok').pack(side=LEFT, expand=YES, fill=X)
        Button(okCancelButtonFrame, text='Cancel', command=lambda: master.destroy()).pack(side=LEFT, expand=YES, fill=X)

    def __makeHelpButtons(self, master):
        helpButtonFrame = Frame(master)
        helpButtonFrame.pack(self.padConf, side=RIGHT)

        Button(helpButtonFrame, text='Добавить гласные',
               command=lambda string=self.vowels: self.__takeStrings(string)).pack(expand=YES, fill=BOTH)
        Button(helpButtonFrame, text='Добавить согласные',
               command=lambda string=self.consonants: self.__takeStrings(string)).pack(expand=YES, fill=BOTH)
        Button(helpButtonFrame, text='Добавить глухие\nсогласные',
               command=lambda string=self.voicelessConsonants: self.__takeStrings(string)).pack(expand=YES, fill=BOTH)
        Button(helpButtonFrame, text='Добавить пробел',
               command=lambda string=self.space: self.__takeStrings(string)).pack(expand=YES, fill=BOTH)
        Button(helpButtonFrame, text='Добавить\n"остальные буквы"',
               command=lambda string=self.otherLetters: self.__takeStrings(string)).pack(expand=YES, fill=BOTH)
        Button(helpButtonFrame, text='Добавить\nудвоение буквы',
               command=lambda string=self.double: self.__takeStrings(string)).pack(expand=YES, fill=BOTH)
        Button(helpButtonFrame, text='Добавить "или"',
               command=lambda string=self.either: self.__takeStrings(string)).pack(expand=YES, fill=BOTH)

    def __takeStrings(self, mark):
        self.text.insert(END, mark)

    def __insertIntoDB(self, dbName):
        pass