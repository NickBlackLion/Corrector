from fileMenu import *
from editMenu import *
from specialMenu import *


class MainMenu:
    def __init__(self, master, mainFrame=None):
        self.mainMenu = Menu(master=master)
        self.fileMenu = FileMenu(master, self.mainMenu, mainFrame)
        self.editMenu = EditMenu(mainMenu=self.mainMenu)
        self.specialMenu = SpecialMenu(mainMenu=self.mainMenu)
        master.config(menu=self.mainMenu)
