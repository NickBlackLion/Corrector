import shelve
from clipboardHandler import *
import os.path


class SpecialMenu:
    def __init__(self, root, mainMenu, mainFrame):
        self.specialMenu = Menu(mainMenu, tearoff=0)
        for value in mainFrame.getCategories():
            self.specialMenu.add_command(label='Добавити {0}'.format(value.lower()),
                                         command=lambda lab=value: self.__makeCommonWindow(lab))

        mainMenu.add_cascade(label='Специальні функції', menu=self.specialMenu)

        self.root = root
        self.textArea = mainFrame.getTextArea()
        self.categories = mainFrame.getCategories()

        self.titles = ['Голосні', 'Приголосні', 'Глухі приголосні',
                       'Пробіл', '"Інші букви"', 'Подвоєння', '"Або"', 'Будь-який символ', 'Цифра', 'Крапка',
                       'Межа слова', 'Межа слова \n-Або-\n Межа слова']
        self.commandsArray = ['[аеєиіїоуюя]', '[бвгґджзйклмнпрстфхцчшщ]', '[пхктшчсц]',
                              '\\s', '\\w+', '{2}', '|', '.', '[0-9]', '\.', '\\b', '\\b|\\b']

        self.frameConf = {'relief': SOLID, 'bd': 1}
        self.padConf = {'padx': 5, 'pady': 5, 'expand': YES, 'fill': BOTH}
        self.areaSize = {'width': 70, 'height': 12}

        self.labels = ['Вирізати', 'Скопіювати', 'Вставити']

    def __makeCommonWindow(self, label):
        self.top = Toplevel(master=self.root)
        self.top.title('Добавити {0}'.format(label.lower()))
        self.top.resizable(False, False)

        if label == self.categories[len(self.categories) - 2]:
            self.__makeHelpButtons(self.top)
            self.__makeEntryFrame(self.top, label)
            self.__makeReplacementText(self.top)
            self.__makeOkCancelButton(self.top, label)
        elif label == self.categories[len(self.categories) - 1]:
            self.__makeHelpButtons(self.top)
            self.__makeEntryFrame(self.top, label)
            self.__makeSynonymText(self.top)
            self.__makeOkCancelButton(self.top, label)
        else:
            self.__makeHelpButtons(self.top)
            self.__makeEntryFrame(self.top, label)
            self.__makeOkCancelButton(self.top, label)

    def __makeEntryFrame(self, master, label):
        entryFrame = Frame(master)
        entryFrame.pack(self.padConf)

        Label(entryFrame, text='Шаблон пошуку').pack()
        self.textPattern = Text(entryFrame, self.areaSize)
        self.checkWordLabel = Label(entryFrame, text='Слово або вираз відсутні у базі', fg='green')

        self.checkWordLabel.pack(expand=YES, fill=X)
        self.textPattern.pack(expand=YES, fill=X)
        self.textPattern.bind('<Button-3>', self.__doPatternPopup)

        Label(entryFrame, text='Коментар').pack()
        self.textHint = Text(entryFrame, self.areaSize)

        self.textHint.pack(expand=YES, fill=X)
        self.textHint.bind('<Button-3>', self.__doHintPopup)

        self.__checkWord(self.top, label)

    def __makeReplacementText(self, master):
        Label(master, text='Яку заміну запропонувати').pack()
        self.textReplace = Text(master, self.areaSize)
        self.textReplace.pack()
        self.textReplace.bind('<Button-3>', self.__doReplacePopup)

    def __makeSynonymText(self, master):
        Label(master, text='Який синонім запропонувати').pack()
        self.textReplace = Text(master, self.areaSize)
        self.textReplace.pack()
        self.textReplace.bind('<Button-3>', self.__doReplacePopup)

    def __makeOkCancelButton(self, master, label):
        okCancelButtonFrame = Frame(master)
        okCancelButtonFrame.pack(self.padConf)

        Button(okCancelButtonFrame, text='Ok',
               command=lambda: self.__insertIntoDB(label)).pack(side=LEFT, expand=YES, fill=X)
        Button(okCancelButtonFrame, text='Cancel',
               command=lambda: master.destroy()).pack(side=LEFT, expand=YES, fill=X)

    def __makeHelpButtons(self, master):
        helpButtonFrame = Frame(master)
        helpButtonFrame.pack(self.padConf, side=RIGHT)

        for index in range(len(self.titles)):
            Button(helpButtonFrame, text=self.titles[index],
                   command=lambda string=self.commandsArray[index]: self.__takeStrings(string))\
                .pack(expand=YES, fill=BOTH)

    def __takeStrings(self, mark):
        self.textPattern.insert(INSERT, mark)

    def __insertIntoDB(self, dbName):
        currPath = os.path.curdir + '//' + dbName

        with shelve.open(currPath + '//' + dbName) as f:
            f[self.textPattern.get('1.0', END).lower()] = self.textHint.get('1.0', END)

        if dbName == self.categories[len(self.categories) - 2] or dbName == self.categories[len(self.categories) - 1]:
            self.__insertRotatingIntoDB(dbName)

        messagebox.showinfo('', 'Слово додане до бази')
        self.top.destroy()

    def __insertRotatingIntoDB(self, dbName):
        currPath = os.path.curdir + '//' + dbName

        with shelve.open(currPath + '//' + dbName + '-rotating') as f:
            f[self.textPattern.get('1.0', END).lower()] = self.textReplace.get('1.0', END)

    def __doPatternPopup(self, event):
        self.__createPatternPopupMenu().tk_popup(event.x_root, event.y_root)

    def __doHintPopup(self, event):
        self.__createHintPopupMenu().tk_popup(event.x_root, event.y_root)

    def __doReplacePopup(self, event):
        self.__createRepacePopupMenu().tk_popup(event.x_root, event.y_root)

    def __createPatternPopupMenu(self):
        popup = Menu(master=self.root, tearoff=0)

        popup.add_command(label=self.labels[0], command=lambda: cutToClipboard(self.root, self.textPattern))
        popup.add_command(label=self.labels[1], command=lambda: copyToClipboard(self.root, self.textPattern))
        popup.add_command(label=self.labels[2], command=lambda: pasteFromClipboard(self.root, self.textPattern))
        return popup

    def __createHintPopupMenu(self):
        popup = Menu(master=self.root, tearoff=0)

        popup.add_command(label=self.labels[0], command=lambda: cutToClipboard(self.root, self.textHint))
        popup.add_command(label=self.labels[1], command=lambda: copyToClipboard(self.root, self.textHint))
        popup.add_command(label=self.labels[2], command=lambda: pasteFromClipboard(self.root, self.textHint))
        return popup

    def __createRepacePopupMenu(self):
        popup = Menu(master=self.root, tearoff=0)

        popup.add_command(label=self.labels[0], command=lambda: cutToClipboard(self.root, self.textReplace))
        popup.add_command(label=self.labels[1], command=lambda: copyToClipboard(self.root, self.textReplace))
        popup.add_command(label=self.labels[2], command=lambda: pasteFromClipboard(self.root, self.textReplace))
        return popup

    def __checkWord(self, top, label):
        isInFile = False
        currPath = os.path.curdir + '//' + label
        currFile = currPath + '//' + label

        if not os.path.exists(currPath):
            os.mkdir(currPath)

        with shelve.open(currFile) as f:
            for key in f.keys():
                if key.strip('\n\r ') == self.textPattern.get('1.0', END).strip('\n\r ').lower():
                    self.checkWordLabel.config(text='Слово або вираз є у базі', fg='red')
                    isInFile = True
                elif not isInFile:
                    self.checkWordLabel.config(text='Слово або вираз відсутні у базі', fg='green')

        top.after(100, self.__checkWord, top, label)
