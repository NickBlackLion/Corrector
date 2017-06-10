from mainFrame import *
from menuBar import *

if __name__ == '__main__':
    root = Tk()
    root.title('Corrector')

    mainframe = MainFrame(master=root)
    MainMenu(master=root, mainFrame=mainframe)

    root.mainloop()
