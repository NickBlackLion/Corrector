from clipboardHandler import *
from searcher import *


class EditMenu:
    def __init__(self, root, mainMenu, mainFrame):
        self.root = root
        self.textArea = mainFrame.getTextArea()

        searcher = Searcher(root=self.root, textArea=self.textArea)
        self.commandArray = ['Отменить Ctrl+Z', 'Вырезать Ctrl+X', 'Копировать Ctrl+C', 'Вставить Ctrl+V', 'Найти...']
        self.functionArray = [lambda: makeBack(self.textArea, mainFrame.getMackBackArray()),
                              lambda: cutToClipboard(self.root, self.textArea, mainFrame.getMackBackArray()),
                              lambda: copyToClipboard(self.root, self.textArea),
                              lambda: pasteFromClipboard(self.root, self.textArea, mainFrame.getMackBackArray()),
                              lambda: searcher.search()]

        self.commandDict = {}

        for index in range(len(self.commandArray)):
            self.commandDict[self.commandArray[index]] = self.functionArray[index]

        self.editMenu = Menu(mainMenu, tearoff=0)

        for index, key in enumerate(self.commandDict):
            if index == 1 or index == 4:
                self.editMenu.add_separator()
            self.editMenu.add_command(label=self.commandArray[index],
                                      command=self.commandDict[self.commandArray[index]])

        mainMenu.add_cascade(label='Правка', menu=self.editMenu)
        mainFrame.getTextArea().bind('<Button-3>', self.__doPopup)

    def __doPopup(self, event):
        self.__createPopupMenu().tk_popup(event.x_root, event.y_root)

    def __createPopupMenu(self):
        popup = Menu(master=self.root, tearoff=0)

        for index in range(4):
            popup.add_command(label=self.commandArray[index], command=self.commandDict[self.commandArray[index]])
        return popup
