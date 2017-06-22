from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from docx import Document


class FileMenu:
    def __init__(self, root, mainMenu=None, mainFrame=None):
        self.commandArray = ['Новий Ctrl+N', 'Вiдкрити Ctrl+O', 'Зберегти Ctrl+S', 'Зберегти як...', 'Вийти']
        self.functionArray = [lambda e=None: self.__newFile(), lambda e=None: self.__openFile(),
                              lambda e=None: self.__saveFile(), lambda e=None: self.__saveAsFile(),
                              lambda e=None: self.__exit()]

        self.commandDict = {}

        self.bindsCommandArray = ['<Control-n>', '<Control-o>', '<Control-s>']

        for index in range(len(self.commandArray)):
            self.commandDict[self.commandArray[index]] = self.functionArray[index]

        self.fileMenu = Menu(mainMenu, tearoff=0)

        for index, key in enumerate(self.commandDict):
            if index == 1 or index == 4:
                self.fileMenu.add_separator()
            self.fileMenu.add_command(label=self.commandArray[index],
                                      command=self.commandDict[self.commandArray[index]])

        mainMenu.add_cascade(label='Файл', menu=self.fileMenu)

        self.fileTypes = (("pictures", "*.docx"), ("all types", "*.*"))
        self.textArea = mainFrame.textArea
        self.mainFrame = mainFrame
        self.root = root
        self.textLength = 0
        self.openFilePath = None

        for index in range(len(self.bindsCommandArray)):
            root.bind(self.bindsCommandArray[index], self.commandDict[self.commandArray[index]])

    def __openFile(self):
        if self.mainFrame.isTextChanged():
            answer = messagebox.askyesnocancel('Открытие файла', 'Вы изменили текст. Хотите его сохранить?')
            if answer is None:
                pass
            elif answer:
                self.__saveFile()
                self.mainFrame.clearTextArea()
                self.__open()
            elif not answer:
                self.mainFrame.clearTextArea()
                self.__open()
        else:
            self.mainFrame.clearTextArea()
            self.__open()

    def __saveFile(self):
        if self.openFilePath:
            self.__save(self.openFilePath.name)
        else:
            self.__saveAsFile()

    def __newFile(self):
        if self.mainFrame.isTextChanged():
            answer = messagebox.askyesnocancel('Новый файл', 'Вы изменили текст. Хотите его сохранить?')
            if answer is None:
                pass
            elif answer:
                self.__saveFile()
                self.mainFrame.clearTextArea()
                self.openFilePath = None
            elif not answer:
                self.mainFrame.clearTextArea()
                self.openFilePath = None
        else:
            self.mainFrame.clearTextArea()
            self.openFilePath = None

    def __exit(self):
        if self.mainFrame.isTextChanged():
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

        self.mainFrame.resetTextSizeChanged()

    def __open(self):
        self.openFilePath = filedialog.askopenfile(filetypes=self.fileTypes)
        if self.openFilePath:
            doc = Document(self.openFilePath.name)
            for paragraph in doc.paragraphs:
                self.textArea.insert(INSERT, paragraph.text)
                self.mainFrame.setTextLength(len(paragraph.text))
                paragraph.clear()
