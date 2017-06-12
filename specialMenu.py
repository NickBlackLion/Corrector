from tkinter import *


class SpecialMenu:
    def __init__(self, mainMenu):
        self.specialMenu = Menu(mainMenu, tearoff=0)
        self.specialMenu.add_command(label='Добавить стоп-слово')
        self.specialMenu.add_command(label='Добавить повторяемое слово')
        self.specialMenu.add_command(label='Добавить устоявшиеся выражения и русизмы')
        self.specialMenu.add_command(label='Добавить чередования')
        self.specialMenu.add_command(label='Добавить синонимы')
        mainMenu.add_cascade(label='Специальные функции', menu=self.specialMenu)
