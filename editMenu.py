from clipboardHandler import *
from searcher import *


class EditMenu:
    def __init__(self, root, mainMenu, mainFrame):
        self.commandArray = ['Отменить Ctrl+Z', 'Вырезать Ctrl+X', 'Копировать Ctrl+C', 'Вставить Ctrl+V', 'Найти...',
                             'Найти далее']
        self.functionArray = [lambda e=None: makeBack(self.textArea, mainFrame.getMackBackArray()),
                              lambda e=None: cutToClipboard(self.root, self.textArea, mainFrame.getMackBackArray()),
                              lambda e=None: copyToClipboard(self.root, self.textArea),
                              lambda e=None: pasteFromClipboard(self.root, self.textArea, mainFrame.getMackBackArray()),
                              lambda e=None: search(self.root, self.textArea),
                              lambda e=None: searchMore()]

        self.commandDict = {}

        self.bindsCommandArray = ['<Control-z>', '<Control-x>', '<Control-c>', '<Control-v>']

        for index in range(len(self.commandArray)):
            self.commandDict[self.commandArray[index]] = self.functionArray[index]

        self.editMenu = Menu(mainMenu, tearoff=0)

        for index, key in enumerate(self.commandDict):
            if index == 1 or index == 4:
                self.editMenu.add_separator()
            self.editMenu.add_command(label=self.commandArray[index],
                                      command=self.commandDict[self.commandArray[index]])

        mainMenu.add_cascade(label='Правка', menu=self.editMenu)

        self.root = root
        self.textArea = mainFrame.getTextArea()
        mainFrame.getTextArea().bind('<Button-3>', self.__doPopup)

        """for index in range(len(self.bindsCommandArray)):
            mainFrame.textArea.bind(self.bindsCommandArray[index], self.commandDict[self.commandArray[index]])"""

        mainFrame.textArea.bind('<Control-v>', lambda e: pasteFromClipboard(self.root, self.textArea,
                                                                          mainFrame.getMackBackArray()))

    def __doPopup(self, event):
        self.__createPopupMenu().tk_popup(event.x_root, event.y_root)

    def __createPopupMenu(self):
        popup = Menu(master=self.root, tearoff=0)

        for index in range(len(self.bindsCommandArray)):
            popup.add_command(label=self.commandArray[index], command=self.commandDict[self.commandArray[index]])
        return popup
