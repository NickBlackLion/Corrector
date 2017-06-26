from tkinter import messagebox
from tkinter import *
import re
import shelve
import os.path
import os


class Searcher:
    def __init__(self, root=None, textArea=None, packCanvas=None):
        self.root = root
        self.textArea = textArea
        self.packCanvas = packCanvas

        self.searchingWord = ''

    def searcher(self, var):
        if var:
            f = None

            try:
                path = getattr(self.packCanvas, 'categoryName')
                currPath = os.path.curdir + '//' + path
                currFile = currPath + '//' + path

                if not os.path.exists(currPath):
                    os.mkdir(currPath)

                f = shelve.open(currFile)
                for i in f:
                    getattr(self.packCanvas, 'allRegex')[i.strip('\n')] = f[i]

            finally:
                f.close()

            if not getattr(self.packCanvas, 'allRegex') and var:
                messagebox.showinfo('Пустая таблица',
                                    'Таблица данной категории не заполнена\nДля работы внесите хотя бы одно слово')

            text = self.textArea.get('1.0', END)
            textRows = re.split('\n', text)

            if var and len(textRows) > 0:
                row = 1

                for oneTextRow in textRows:
                    for reg in getattr(self.packCanvas, 'allRegex'):
                        summ = 0
                        firstMatched = 0
                        lastMatched = 0

                        while summ <= len(oneTextRow):
                            matched = re.search(reg, oneTextRow[summ:], re.IGNORECASE)

                            if matched is not None:
                                firstMatched = summ + matched.start()
                                lastMatched = summ + matched.end()

                                summ += int(matched.end())
                                self.textArea.tag_add('text', '1.0', '{0}.{1}'.format(row, firstMatched))
                                self.textArea.tag_add('text', '{0}.{1}'.format(row, lastMatched), END)
                                self.textArea.tag_add(reg, '{0}.{1}'.format(row, firstMatched),
                                                      '{0}.{1}'.format(row, lastMatched))
                                self.textArea.tag_configure(reg, background=getattr(self.packCanvas, 'color'))
                                self.textArea.tag_raise("sel")

                            if not lastMatched or matched is None:
                                break

                        self.textArea.tag_bind(reg, '<Button-1>', lambda e, r=reg: self.packCanvas.createHint(e, r))
                        self.textArea.tag_bind('text', '<Button-1>', self.packCanvas.deleteHint)

                    row += 1
        else:
            for reg in getattr(self.packCanvas, 'allRegex'):
                self.textArea.tag_delete(reg)

    def search(self):
        self.topWin = Toplevel(self.root)
        self.topWin.title('Найти')

        frame = Frame(self.topWin)
        frame.pack(expand=YES, fill=BOTH)
        textLine = Text(frame, width=40, height=3)
        textLine.pack(expand=YES, fill=X)

        Button(frame, text='Найти', command=lambda: self.searchOne(textLine.get('1.0', END))).pack(side=LEFT, expand=YES, fill=X)
        Button(frame, text='Отмена', command=lambda: self.destroySearchWin()).pack(side=LEFT, expand=YES, fill=X)

    def searchOne(self, searchingWord):
        self.textArea.tag_delete(self.searchingWord)
        self.searchingWord = searchingWord.strip()

        text = self.textArea.get('1.0', END)
        textRows = re.split('\n', text)

        row = 1

        for oneTextRow in textRows:
            summ = 0
            firstMatched = 0
            lastMatched = 0

            while summ <= len(oneTextRow):
                matched = re.search(self.searchingWord, oneTextRow[summ:], re.IGNORECASE)

                if matched is not None:
                    firstMatched = summ + matched.start()
                    lastMatched = summ + matched.end()

                    summ += int(matched.end())
                    self.textArea.tag_add('text', '1.0', '{0}.{1}'.format(row, firstMatched))
                    self.textArea.tag_add('text', '{0}.{1}'.format(row, lastMatched), END)
                    self.textArea.tag_add(self.searchingWord, '{0}.{1}'.format(row, firstMatched),
                                        '{0}.{1}'.format(row, lastMatched))
                    self.textArea.tag_configure(self.searchingWord, background='grey')
                    self.textArea.tag_raise("sel")

                if not lastMatched or matched is None:
                    break

            row += 1

    def destroySearchWin(self):
        self.textArea.tag_delete(self.searchingWord)
        self.topWin.destroy()
