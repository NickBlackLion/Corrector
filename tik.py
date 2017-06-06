from tkinter import *
import re


def foo1(textArea, checkVar):
    allRegex = []
    with open('data.txt') as f:
        for x in f:
            allRegex.append(x.strip('\n'))

    text = textArea.get('1.0', END)
    textRows = re.split('\n', text)

    if checkVar and len(textRows) > 0:
        row = 1

        for oneTextRow in textRows:
            for reg in allRegex:
                summ = 0
                firstMatched = 0
                lastMatched = 0

                while summ <= len(oneTextRow):
                    matched = re.search(reg, oneTextRow[summ:])

                    if matched != None:
                        firstMatched = summ + matched.start()
                        lastMatched = summ + matched.end()

                        summ += int(matched.end())
                        textArea.tag_add('start', '{0}.{1}'.format(row, firstMatched),
                                         '{0}.{1}'.format(row, lastMatched))
                        textArea.tag_configure('start', background='yellow')
                        textArea.tag_raise("sel")

                    if not lastMatched or matched is None:
                        break

            row += 1
    else:
        textArea.tag_delete('start')


if __name__ == "__main__":
    root = Tk()
    root.title('Corrector')

    sinonimFrame = Frame(master=root)
    textFrame = Frame(master=root)

    var1 = IntVar()
    var2 = IntVar()

    ch1 = Checkbutton(master=sinonimFrame, text='Орфография',
                      variable=var1, command=lambda: foo1(textArea, var1.get()))
    ch2 = Checkbutton(master=sinonimFrame, text='Пунктуация',
                      variable=var2)

    ch1.pack()
    ch2.pack()

    textArea = Text(master=textFrame)
    textArea.config(selectbackground='green')

    scrollBar = Scrollbar(master=textFrame)
    sinonimArea = Text(master=sinonimFrame)
    sinonimArea.pack()

    textArea.config(yscrollcommand=scrollBar.set)
    scrollBar.config(command=textArea.yview)

    sinonimFrame.pack(side=RIGHT, fill=Y)
    textFrame.pack(side=LEFT, fill=Y)
    textArea.pack(side=LEFT, fill=Y, expand=YES)
    scrollBar.pack(side=RIGHT, fill=Y, expand=YES)

    menuBar = Menu(root)

    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label='New')
    fileMenu.add_separator()
    fileMenu.add_command(label='Open')
    fileMenu.add_command(label='Save')
    fileMenu.add_command(label='Save As...')
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit')
    menuBar.add_cascade(label='File', menu=fileMenu)

    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label='Cancel')
    editMenu.add_separator()
    editMenu.add_command(label='Cut')
    editMenu.add_command(label='Copy')
    editMenu.add_command(label='Paste')
    editMenu.add_separator()
    editMenu.add_command(label='Find')
    editMenu.add_command(label='Find next')
    editMenu.add_command(label='Replace')
    editMenu.add_command(label='Move to')
    menuBar.add_cascade(label='Edit', menu=editMenu)

    specMenu = Menu(menuBar, tearoff=0)
    specMenu.add_command(label='Wunder vafles1')
    specMenu.add_command(label='Wunder vafles2')
    specMenu.add_command(label='Wunder vafles3')
    specMenu.add_separator()
    specMenu.add_command(label='Wunder vafles4')
    specMenu.add_command(label='Wunder vafles5')
    specMenu.add_command(label='Wunder vafles6')
    specMenu.add_command(label='Wunder vafles7')
    menuBar.add_cascade(label='Special', menu=specMenu)

    root.config(menu=menuBar)
    root.mainloop()
