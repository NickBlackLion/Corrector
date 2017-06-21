from tkinter import messagebox
from tkinter import *
import re
import shelve


def searcher(var, textArea, PackCanvas):
    if var:
        f = None

        try:
            f = shelve.open(getattr(PackCanvas, 'categoryName'))
            for i in f:
                getattr(PackCanvas, 'allRegex')[i.strip('\n')] = f[i]

        finally:
            f.close()

        if not getattr(PackCanvas, 'allRegex') and var:
            messagebox.showinfo('Пустая таблица',
                                'Таблица данной категории не заполнена\nДля работы внесите хотя бы одно слово')

        text = textArea.get('1.0', END)
        textRows = re.split('\n', text)

        if var and len(textRows) > 0:
            row = 1

            for oneTextRow in textRows:
                for reg in getattr(PackCanvas, 'allRegex'):
                    summ = 0
                    firstMatched = 0
                    lastMatched = 0

                    while summ <= len(oneTextRow):
                        matched = re.search(reg, oneTextRow[summ:], re.IGNORECASE)

                        if matched is not None:
                            firstMatched = summ + matched.start()
                            lastMatched = summ + matched.end()

                            summ += int(matched.end())
                            textArea.tag_add('text', '1.0', '{0}.{1}'.format(row, firstMatched))
                            textArea.tag_add('text', '{0}.{1}'.format(row, lastMatched), END)
                            textArea.tag_add(reg, '{0}.{1}'.format(row, firstMatched),
                                             '{0}.{1}'.format(row, lastMatched))
                            textArea.tag_configure(reg, background=getattr(PackCanvas, 'color'))
                            textArea.tag_raise("sel")
                            setattr(PackCanvas, 'hint', getattr(PackCanvas, 'allRegex')[reg])

                        if not lastMatched or matched is None:
                            break

                    textArea.tag_bind(reg, '<Button-1>', getattr(PackCanvas, 'createFoo'))
                    textArea.tag_bind('text', '<Button-1>', getattr(PackCanvas, 'deleteFoo'))

                row += 1
    else:
        for reg in getattr(PackCanvas, 'allRegex'):
            textArea.tag_delete(reg)


def search(root, textArea=None):
    topWin = Toplevel(root)
    topWin.title('Найти')

    frame = Frame(topWin)
    frame.pack(expand=YES, fill=BOTH)
    textLine = Entry(frame)
    textLine.pack(expand=YES, fill=X)

    Button(frame, text='Найти').pack(side=LEFT, expand=YES, fill=X)
    Button(frame, text='Отмена', command=lambda: topWin.destroy()).pack(side=LEFT, expand=YES, fill=X)


def searchMore():
    pass
