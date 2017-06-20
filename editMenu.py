from tkinter import *
from tkinter import messagebox


class EditMenu:
    def __init__(self, root, mainMenu, mainFrame):
        self.commandArray = ['Вырезать Ctrl+X', 'Копировать Ctrl+C', 'Вставить Ctrl+V', 'Отменить Ctrl+Z']
        self.commandDict = {self.commandArray[0]: lambda: self.__cutToClipboard(),
                            self.commandArray[1]: lambda: self.__copyToClipboard(),
                            self.commandArray[2]: lambda: self.__pasteFromClipboard(),
                            self.commandArray[3]: lambda: self.__makeBack()}
        self.editMenu = Menu(mainMenu, tearoff=0)
        self.editMenu.add_command(label=self.commandArray[3], command=self.commandDict[self.commandArray[3]])
        self.editMenu.add_separator()
        self.editMenu.add_command(label=self.commandArray[0], command=self.commandDict[self.commandArray[0]])
        self.editMenu.add_command(label=self.commandArray[1], command=self.commandDict[self.commandArray[1]])
        self.editMenu.add_command(label=self.commandArray[2], command=self.commandDict[self.commandArray[2]])
        self.editMenu.add_separator()
        self.editMenu.add_command(label='Найти...')
        self.editMenu.add_command(label='Найти далее')
        mainMenu.add_cascade(label='Правка', menu=self.editMenu)

        self.root = root
        self.textArea = mainFrame.getTextArea()
        mainFrame.getTextArea().bind('<Button-3>', self.__doPopup)

        mainFrame.textArea.bind('<Control-x>', lambda e: self.commandDict[self.commandArray[0]])
        mainFrame.textArea.bind('<Control-c>', lambda e: self.commandDict[self.commandArray[1]])
        mainFrame.textArea.bind('<Control-v>', lambda e: self.commandDict[self.commandArray[2]])
        mainFrame.textArea.bind('<Control-z>', lambda e: self.commandDict[self.commandArray[3]])

        self.makeBackArray = []

    def __doPopup(self, event):
        self.__createPopupMenu().tk_popup(event.x_root, event.y_root)

    def __createPopupMenu(self):
        popup = Menu(master=self.root, tearoff=0)
        popup.add_command(label=self.commandArray[3], command=self.commandDict[self.commandArray[3]])
        popup.add_command(label=self.commandArray[0], command=self.commandDict[self.commandArray[0]])
        popup.add_command(label=self.commandArray[1], command=self.commandDict[self.commandArray[1]])
        popup.add_command(label=self.commandArray[2], command=self.commandDict[self.commandArray[2]])
        return popup

    def __copyToClipboard(self):
        try:
            fromClipboard = self.root.clipboard_get()
        except TclError:
            fromClipboard = ''

        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.textArea.get(SEL_FIRST, SEL_LAST))
        except TclError:
            self.root.clipboard_append(fromClipboard)

    def __pasteFromClipboard(self):
        self.makeBackArray.append(self.textArea.get('1.0', END))

        try:
            self.textArea.delete(SEL_FIRST, SEL_LAST)
        except TclError:
            try:
                self.textArea.insert(CURRENT, self.root.clipboard_get())
            except TclError:
                messagebox.showinfo('', 'В буффере пусто')


    def __cutToClipboard(self):
        self.makeBackArray.append(self.textArea.get('1.0', END))

        try:
            fromClipboard = self.root.clipboard_get()
        except TclError:
            fromClipboard = ''

        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.textArea.get(SEL_FIRST, SEL_LAST))
            self.textArea.delete(SEL_FIRST, SEL_LAST)
        except TclError:
            self.root.clipboard_append(fromClipboard)

    def __makeBack(self):
        print('in  __makeBack')
        if len(self.makeBackArray) > 0:
            self.textArea.delete('1.0', END)
            self.textArea.insert('1.0', self.makeBackArray.pop().strip('\n'))
