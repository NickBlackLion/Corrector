import shelve
from clipboardHandler import *


class SpecialMenu:
    def __init__(self, root, mainMenu, mainFrame):
        self.commandArray = ['Вырезать Ctrl+X', 'Копировать Ctrl+C', 'Вставить Ctrl+V', 'Отменить Ctrl+Z']
        self.patternDict = {self.commandArray[0]: lambda: cutToClipboard(self.root, self.pattern),
                            self.commandArray[1]: lambda: copyToClipboard(self.root, self.pattern),
                            self.commandArray[2]: lambda: pasteFromClipboard(self.root, self.pattern)}

        self.hintDict = {self.commandArray[0]: lambda: cutToClipboard(self.root, self.hint),
                         self.commandArray[1]: lambda: copyToClipboard(self.root, self.hint),
                         self.commandArray[2]: lambda: pasteFromClipboard(self.root, self.hint)}

        self.specialMenu = Menu(mainMenu, tearoff=0)
        for value in mainFrame.getCategories():
            self.specialMenu.add_command(label='Добавить {0}'.format(value.lower()), command=lambda lab=value: self.__makeCommonWindow(lab))
        mainMenu.add_cascade(label='Специальные функции', menu=self.specialMenu)

        self.root = root
        self.mainFrame = mainFrame

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
        self.pattern.bind('<Button-3>', self.__doPatternPopup)

        Label(entryFrame, text='Комментарий').pack()
        self.hint = Text(entryFrame, areaSize)
        self.hint.pack(expand=YES, fill=X)
        self.hint.bind('<Button-3>', self.__doHintPopup)

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

    def __doPatternPopup(self, event):
        self.__createPatternPopupMenu().tk_popup(event.x_root, event.y_root)

    def __doHintPopup(self, event):
        self.__createHintPopupMenu().tk_popup(event.x_root, event.y_root)

    def __createPatternPopupMenu(self):
        popup = Menu(master=self.root, tearoff=0)
        popup.add_command(label=self.commandArray[3], command=self.patternDict[self.commandArray[3]])
        popup.add_command(label=self.commandArray[0], command=self.patternDict[self.commandArray[0]])
        popup.add_command(label=self.commandArray[1], command=self.patternDict[self.commandArray[1]])
        popup.add_command(label=self.commandArray[2], command=self.patternDict[self.commandArray[2]])
        return popup

    def __createHintPopupMenu(self):
        popup = Menu(master=self.root, tearoff=0)
        popup.add_command(label=self.commandArray[3], command=self.hintDict[self.commandArray[3]])
        popup.add_command(label=self.commandArray[0], command=self.hintDict[self.commandArray[0]])
        popup.add_command(label=self.commandArray[1], command=self.hintDict[self.commandArray[1]])
        popup.add_command(label=self.commandArray[2], command=self.hintDict[self.commandArray[2]])
        return popup
