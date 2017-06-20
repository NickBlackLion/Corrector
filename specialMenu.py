from tkinter import *
import shelve
from tkinter import messagebox


class SpecialMenu:
    def __init__(self, root, mainMenu, mainFrame):
        self.specialMenu = Menu(mainMenu, tearoff=0)
        for value in mainFrame.getCategoryes():
            self.specialMenu.add_command(label='Добавить {0}'.format(value.lower()), command=lambda lab=value: self.__makeCommonWindow(lab))
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
        self.top = Toplevel(master=self.root)
        self.top.title('Добавить {0}'.format(label.lower()))

        self.__makeHelpButtons(self.top)
        self.__makeEntryFrame(self.top)
        self.__makeOkCancelButton(self.top, label)

    def __makeEntryFrame(self, master):
        areaSize = {'width': 70, 'height': 10}

        entryFrame = Frame(master)
        entryFrame.pack(self.padConf)

        Label(entryFrame, text='Шаблон поиска').pack()
        self.pattern = Text(entryFrame, areaSize)
        self.pattern.pack(expand=YES, fill=X)

        Label(entryFrame, text='Комментарий').pack()
        self.hint = Text(entryFrame, areaSize)
        self.hint.pack(expand=YES, fill=X)

    def __makeOkCancelButton(self, master, label):
        okCancelButtonFrame = Frame(master)
        okCancelButtonFrame.pack(self.padConf)

        Button(okCancelButtonFrame, text='Ok', command=lambda: self.__insertIntoDB(label)).pack(side=LEFT, expand=YES, fill=X)
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
        self.pattern.insert(END, mark)

    def __insertIntoDB(self, dbName):
        with shelve.open(dbName) as f:
            f[self.pattern.get('1.0', END)] = self.hint.get('1.0', END)
        messagebox.showinfo('', 'Слово добавленно в базу')
        self.top.destroy()
