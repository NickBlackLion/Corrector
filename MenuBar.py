from FileMenu import *

class MainMenu:
    def __init__(self, master):
        self.mainMenu = Menu(master=master)
        self.fileMenu = FileMenu(self.mainMenu)
        master.config(menu=self.mainMenu)
