from tkinter import *


class EditMenu:
    def __init__(self, mainMenu):
        self.editMenu = Menu(mainMenu, tearoff=0)
        self.editMenu.add_command(label='Отменить')
        self.editMenu.add_separator()
        self.editMenu.add_command(label='Вырезать')
        self.editMenu.add_command(label='Копировать')
        self.editMenu.add_command(label='Вставить')
        self.editMenu.add_separator()
        self.editMenu.add_command(label='Найти...')
        self.editMenu.add_command(label='Найти далее')
        mainMenu.add_cascade(label='Правка', menu=self.editMenu)
