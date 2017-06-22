from tkinter import *
from tkinter import messagebox


def copyToClipboard(root, textArea):
    try:
        fromClipboard = root.clipboard_get()
    except TclError:
        fromClipboard = ''

    try:
        root.clipboard_clear()
        root.clipboard_append(textArea.get(SEL_FIRST, SEL_LAST))
    except TclError:
        root.clipboard_append(fromClipboard)


def pasteFromClipboard(root, textArea, makeBackArray=None):
    if makeBackArray is not None:
        makeBackArray.append(textArea.get('1.0', END))

    try:
        textArea.delete(SEL_FIRST, SEL_LAST)
        textArea.insert(CURRENT, root.clipboard_get())
    except TclError:
        try:
            textArea.insert(CURRENT, root.clipboard_get())
        except TclError:
            messagebox.showinfo('', 'В буффере пусто')


def cutToClipboard(root, textArea, makeBackArray=None):
    if makeBackArray is not None:
        makeBackArray.append(textArea.get('1.0', END))

    try:
        fromClipboard = root.clipboard_get()
    except TclError:
        fromClipboard = ''

    try:
        root.clipboard_clear()
        textArea.delete(SEL_FIRST, SEL_LAST)
    except TclError:
        root.clipboard_append(fromClipboard)


def makeBack(textArea, makeBackArray=None):
    if makeBackArray is not None and len(makeBackArray) > 0:
        textArea.delete('1.0', END)
        textArea.insert('1.0', makeBackArray.pop().strip('\n'))
