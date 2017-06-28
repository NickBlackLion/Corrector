from mainFrame import *
from menuBar import *
from editMenu import *

if __name__ == '__main__':
    root = Tk()
    root.title('Коректор')
    root.resizable(False, True)

    mainframe = MainFrame(master=root)
    MainMenu(master=root, mainFrame=mainframe)

    root.mainloop()
