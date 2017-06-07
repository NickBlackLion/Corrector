from tkinter import *


class FileMenu:
    def __init__(self, mainMenu):
        self.fileMenu = Menu(mainMenu, tearoff=0)
        self.fileMenu.add_command(label='Новий')
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Вiдкрити')
        self.fileMenu.add_command(label='Зберегти')
        self.fileMenu.add_command(label='Зберегти як...')
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Вийти')
        mainMenu.add_cascade(label='Файл', menu=self.fileMenu)
