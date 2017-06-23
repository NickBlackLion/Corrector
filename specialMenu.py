import shelve
from clipboardHandler import *


class SpecialMenu:
    def __init__(self, root, mainMenu, mainFrame):
        self.specialMenu = Menu(mainMenu, tearoff=0)
        for value in mainFrame.getCategories():
            self.specialMenu.add_command(label='Добавить {0}'.format(value.lower()),
                                         command=lambda lab=value: self.__makeCommonWindow(lab))

        mainMenu.add_cascade(label='Специальные функции', menu=self.specialMenu)

        self.root = root
        self.textArea = mainFrame.getTextArea()

        self.titles = ['Добавить гласные', 'Добавить согласные', 'Добавить глухие\nсогласные',
                       'Добавить пробел', 'Добавить\n"остальные буквы"', 'Добавить\nудвоение буквы', 'Добавить "или"']
        self.commandsArray = ['[аеєиіїоуюя]', '[бвгґджзйклмнпрстфхцчшщ]', '[пхктшчсц]', '\\s', '\\w+', '{2}', '|']

        self.frameConf = {'relief': SOLID, 'bd': 1}
        self.padConf = {'padx': 5, 'pady': 5, 'expand': YES, 'fill': BOTH}

    def __makeCommonWindow(self, label):
        self.top = Toplevel(master=self.root)
        self.top.title('Добавить {0}'.format(label.lower()))

        self.__makeHelpButtons(self.top)
        self.__makeEntryFrame(self.top, label)
        self.__makeOkCancelButton(self.top, label)

    def __makeEntryFrame(self, master, label):
        areaSize = {'width': 70, 'height': 10}

        entryFrame = Frame(master)
        entryFrame.pack(self.padConf)

        Label(entryFrame, text='Шаблон поиска').pack()
        self.pattern = Text(entryFrame, areaSize)
        self.checkWordLabel = Label(entryFrame, text='Слово или выражение отсутствует в базе', fg='green')

        self.checkWordLabel.pack(expand=YES, fill=X)
        self.pattern.pack(expand=YES, fill=X)
        self.pattern.bind('<Button-3>', self.__doPatternPopup)

        Label(entryFrame, text='Комментарий').pack()
        self.hint = Text(entryFrame, areaSize)

        self.hint.pack(expand=YES, fill=X)
        self.hint.bind('<Button-3>', self.__doHintPopup)

        self.__checkWord(self.top, label)

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

        popup.add_command(label='Вырезать', command=lambda: cutToClipboard(self.root, self.pattern))
        popup.add_command(label='Копировать', command=lambda: copyToClipboard(self.root, self.pattern))
        popup.add_command(label='Вставить', command=lambda: pasteFromClipboard(self.root, self.pattern))
        return popup

    def __createHintPopupMenu(self):
        popup = Menu(master=self.root, tearoff=0)

        popup.add_command(label='Вырезать', command=lambda: cutToClipboard(self.root, self.hint))
        popup.add_command(label='Копировать', command=lambda: copyToClipboard(self.root, self.hint))
        popup.add_command(label='Вставить', command=lambda: pasteFromClipboard(self.root, self.hint))
        return popup

    # TODO Подумать над конструкцие, как выводить тот или иной маркер при наличии
    # TODO отсутствии ключа
    def __checkWord(self, top, label):
        with shelve.open(label) as f:
            for key in f.keys():
                print(key.strip('\n\r ') == self.pattern.get('1.0', END).strip('\n\r '))
                if key.strip('\n\r ') == self.pattern.get('1.0', END).strip('\n\r '):
                    self.checkWordLabel.config(text='Слово или конструкция уже есть в базе', fg='red')
                else:
                    self.checkWordLabel.config(text='Слово или выражение отсутствует в базе', fg='green')

        top.after(100, self.__checkWord, top, label)
