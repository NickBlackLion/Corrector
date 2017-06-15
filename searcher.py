from tkinter import END
from tkinter import messagebox
import re


def searcher(var, textArea, allRegex, func1, func2, categoryName=None, color=None):
    if var:
        f = None

        try:
            f = open(categoryName, 'r', encoding='utf-8')
            for i in f:
                allRegex.append(i.strip('\r\n'))
        except FileNotFoundError:
            open(categoryName, 'w').close()
        finally:
            if f is not None:
                f.close()

        if not allRegex and var:
            messagebox.showinfo('Пустая таблица',
                                'Таблица данной категории не заполнена\nДля работы внесите хотя бы одно слово')

        text = textArea.get('1.0', END)
        textRows = re.split('\n', text)

        if var and len(textRows) > 0:
            row = 1

            for oneTextRow in textRows:
                for reg in allRegex:
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
                            textArea.tag_configure(reg, background=color)
                            textArea.tag_raise("sel")

                        if not lastMatched or matched is None:
                            break

                    textArea.tag_bind(reg, '<Button-1>', func1)
                    textArea.tag_bind('text', '<Button-1>', func2)

                row += 1
    else:
        for reg in allRegex:
            textArea.tag_delete(reg)