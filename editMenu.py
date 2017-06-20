from clipboardHandler import *


class EditMenu:
    def __init__(self, root, mainMenu, mainFrame):
        self.commandArray = ['Вырезать Ctrl+X', 'Копировать Ctrl+C', 'Вставить Ctrl+V', 'Отменить Ctrl+Z']
        self.commandDict = {self.commandArray[0]: lambda: cutToClipboard(self.root, self.textArea, mainFrame.getMackBackArray()),
                            self.commandArray[1]: lambda: copyToClipboard(self.root, self.textArea),
                            self.commandArray[2]: lambda: pasteFromClipboard(self.root, self.textArea, mainFrame.getMackBackArray()),
                            self.commandArray[3]: lambda: makeBack(self.textArea, mainFrame.getMackBackArray())}

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

    def __doPopup(self, event):
        self.__createPopupMenu().tk_popup(event.x_root, event.y_root)

    def __createPopupMenu(self):
        popup = Menu(master=self.root, tearoff=0)
        popup.add_command(label=self.commandArray[3], command=self.commandDict[self.commandArray[3]])
        popup.add_command(label=self.commandArray[0], command=self.commandDict[self.commandArray[0]])
        popup.add_command(label=self.commandArray[1], command=self.commandDict[self.commandArray[1]])
        popup.add_command(label=self.commandArray[2], command=self.commandDict[self.commandArray[2]])
        return popup
