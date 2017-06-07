from MainFrame import *
from MenuBar import *

if __name__ == '__main__':
    root = Tk()
    root.title('Corrector')

    mainframe = MainFrame(master=root)
    MainMenu(master=root)

    root.mainloop()
