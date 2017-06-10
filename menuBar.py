from fileMenu import *


class MainMenu:
    def __init__(self, master, mainFrame=None):
        self.mainMenu = Menu(master=master)
        self.fileMenu = FileMenu(master, self.mainMenu, mainFrame)
        master.config(menu=self.mainMenu)
