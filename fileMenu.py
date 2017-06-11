from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from docx import Document


class FileMenu:
    def __init__(self, root, mainMenu=None, mainFrame=None):
        self.fileMenu = Menu(mainMenu, tearoff=0)
        self.fileMenu.add_command(label='Новий', command=lambda: self.__newFile())
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Вiдкрити Ctrl+O', command=lambda: self.__openFile())
        self.fileMenu.add_command(label='Зберегти', command=lambda: self.__saveFile())
        self.fileMenu.add_command(label='Зберегти як...', command=lambda: self.__saveAsFile())
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Вийти', command=lambda: self.__exit())
        mainMenu.add_cascade(label='Файл', menu=self.fileMenu)

        self.fileTypes = (("pictures", "*.docx"), ("all types", "*.*"))
        self.textArea = mainFrame.textArea
        self.mainFrame = mainFrame
        self.root = root
        self.textLength = 0
        self.openFilePath = None

        root.bind('<Control-o>', lambda e: self.__openFile())
        root.bind('<Control-s>', lambda e: self.__saveFile())
        root.bind('<Control-n>', lambda e: self.__newFile())

    def __openFile(self):
        self.openFilePath = filedialog.askopenfile(filetypes=self.fileTypes)
        if self.openFilePath:
            doc = Document(self.openFilePath.name)
            for paragraph in doc.paragraphs:
                self.textArea.insert(INSERT, paragraph.text)
                self.mainFrame.setTextLength(len(paragraph.text))
                paragraph.clear()

    def __saveFile(self):
        if self.openFilePath:
            self.__save(self.openFilePath.name)
        else:
            self.__saveAsFile()

    def __newFile(self):
        if self.mainFrame.isTextSizeChanged:
            answer = messagebox.askyesnocancel('Новый файл', 'Вы изменили текст. Хотите его сохранить?')
            if answer is None:
                pass
            elif answer:
                self.__saveFile()
                self.mainFrame.clearTextArea()
            elif not answer:
                self.mainFrame.clearTextArea()
        else:
            self.mainFrame.clearTextArea()

    def __exit(self):
        if self.mainFrame.isTextSizeChanged:
            answer = messagebox.askyesnocancel('Выход', 'Вы изменили текст. Хотите его сохранить?')
            if answer is None:
                pass
            elif answer:
                self.__saveFile()
                self.root.quit()
            elif not answer:
                self.root.quit()
        else:
            self.root.quit()

    def __saveAsFile(self):
        self.saveFilePath = filedialog.asksaveasfile(filetypes=self.fileTypes)
        if self.saveFilePath:
            self.__save(self.saveFilePath.name)

    def __save(self, pathToFile):
        doc = Document()
        doc.add_paragraph(self.textArea.get('1.0', END).strip('\n'))
        doc.save(str(pathToFile))
        messagebox.showinfo('Сохранение файла', 'Файл сохранен')
        for paragraph in doc.paragraphs:
            self.mainFrame.setTextLength(len(paragraph.text))
