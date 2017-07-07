from mainFrame import *
from menuBar import *
from editMenu import *
import shutil

if __name__ == '__main__':
    root = Tk()
    root.title('Коректор')
    root.resizable(False, True)

    mainframe = MainFrame(master=root)
    MainMenu(master=root, mainFrame=mainframe)

    mainDirectory = None
    backUpDirectory = None

    with open('pathways', encoding='utf-8') as f:
        mainDirectory = f.readline()
        backUpDirectory = f.readline()

    if mainDirectory == 'None' or backUpDirectory == 'None':
        messagebox.showwarning(title='Додавання шляхів БД',
                               message='Задайте будь ласка шлаяхи для збереження та\nрезервного копіювання бази')
    else:
        if not os.path.exists(mainDirectory.strip('\n')):
            os.mkdir(mainDirectory.strip('\n'))

        if os.path.exists(backUpDirectory.strip('\n')):
            shutil.rmtree(backUpDirectory.strip('\n'))

        shutil.copytree(mainDirectory.strip('\n'), backUpDirectory.strip('\n'))

    root.mainloop()
