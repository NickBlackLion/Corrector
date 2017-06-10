from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from docx import Document


class FileMenu:
    def __init__(self, root, mainMenu=None, mainFrame=None):
        self.fileMenu = Menu(mainMenu, tearoff=0)
        self.fileMenu.add_command(label='Новий', command=lambda: self.__newFile())
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Вiдкрити', command=lambda: self.__openFile())
        self.fileMenu.add_command(label='Зберегти', command=lambda: self.__saveFile())
        self.fileMenu.add_command(label='Зберегти як...')
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Вийти', command=lambda: self.__exit())
        mainMenu.add_cascade(label='Файл', menu=self.fileMenu)

        self.fileTypes = (("pictures", "*.docx"), ("all types", "*.*"))
        self.textArea = mainFrame.textArea
        self.mainFrame = mainFrame
        self.root = root
        self.textLength = 0

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
            doc = Document()
            doc.add_paragraph(self.textArea.get('1.0', END).strip('\n'))
            doc.save(self.openFilePath.name)
            messagebox.showinfo('Сохранение файла', 'Файл сохранен')
            self.mainFrame.cancelWorkCycle()

    def __newFile(self):
        if self.mainFrame.isTextSizeChanged:
            answer = messagebox.askyesnocancel('', 'Вы изменили текст. Хотите его сохранить?')
            if answer:
                self.__saveFile()
                self.mainFrame.clearTextArea()
            else:
                self.mainFrame.clearTextArea()
        else:
            self.textArea.delete('1.0', END)

    def __exit(self):
        if self.mainFrame.isTextSizeChanged:
            answer = messagebox.askyesnocancel('', 'Вы изменили текст. Хотите его сохранить?')
            if answer:
                self.__saveFile()
                self.root.quit()
            else:
                self.root.quit()
        else:
            self.root.quit()

    def __clearAndSave(self):
        answer = messagebox.askyesnocancel('', 'Вы изменили текст. Хотите его сохранить?')
        if answer:
            self.__saveFile()
            self.mainFrame.clearTextArea()
        else:
            self.mainFrame.clearTextArea()
