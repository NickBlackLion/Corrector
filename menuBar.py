from fileMenu import *
from editMenu import *
from specialMenu import *


class MainMenu:
    def __init__(self, master, mainFrame=None):
        self.mainMenu = Menu(master=master)
        self.fileMenu = FileMenu(master, self.mainMenu, mainFrame)
        self.editMenu = EditMenu(master, self.mainMenu, mainFrame)
        self.specialMenu = SpecialMenu(master, self.mainMenu, mainFrame)
        master.config(menu=self.mainMenu)
