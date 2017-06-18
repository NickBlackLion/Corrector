from tkinter import *


class SpecialMenu:
    def __init__(self, root, mainMenu, mainFrame):
        self.specialMenu = Menu(mainMenu, tearoff=0)
        self.specialMenu.add_command(label='Добавить стоп-слово', command=lambda: self.__makeCommonWindow())
        self.specialMenu.add_command(label='Добавить повторяемое слово')
        self.specialMenu.add_command(label='Добавить устоявшиеся выражения и русизмы')
        self.specialMenu.add_command(label='Добавить чередования')
        self.specialMenu.add_command(label='Добавить синонимы')
        mainMenu.add_cascade(label='Специальные функции', menu=self.specialMenu)

        self.root = root

    def __makeCommonWindow(self):
        top = Toplevel(master=self.root)
        top.title('Добавить')
