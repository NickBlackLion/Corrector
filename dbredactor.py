import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget,\
    QTableWidgetItem, QVBoxLayout, QPushButton, QHBoxLayout, QTextEdit, QLabel
import shelve


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Редагування бази даних')
        self.resize(1100, 300)
        self.mainLayout = QHBoxLayout()
        self.count = 0
        self.path = None
        self.categories = []

        self.titles = ['Голосні', 'Приголосні', 'Глухі приголосні',
                       'Пробіл', '"Інші букви"', 'Подвоєння', '"Або"', 'Будь-який символ', 'Цифра', 'Крапка',
                       'Межа слова', 'Межа слова \n-Або-\n Межа слова']

        self.__loadCategories()
        self.__loadData()
        self.__createTabele()
        self.__uploadDataToTable()
        self.__createTextFilds()
        self.__createButton()

        self.setLayout(self.mainLayout)
        self.show()

    def __createTabele(self):
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setRowCount(self.count)
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.mainLayout.addLayout(layout)

    def __createTextFilds(self):
        lab1 = QLabel('Шаблон пошуку')
        lab2 = QLabel('Коментар')
        self.patternArea = QTextEdit()
        self.hintArea = QTextEdit()
        self.okButton = QPushButton('Ok')
        self.cancelButton = QPushButton('Cancel')

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.okButton)
        buttonLayout.addWidget(self.cancelButton)

        layout = QVBoxLayout()
        layout.addWidget(lab1)
        layout.addWidget(self.patternArea)
        layout.addWidget(lab2)
        layout.addWidget(self.hintArea)
        layout.addLayout(buttonLayout)
        self.mainLayout.addLayout(layout)

    def __createButton(self):
        layout = QVBoxLayout()

        for value in self.titles:
            butt = QPushButton(value)
            layout.addWidget(butt)

        self.mainLayout.addLayout(layout)

    def __loadCategories(self):
        with open('categoryes', encoding='utf-8') as f:
            for value in f:
                self.categories.append(value)

    def __loadData(self):
        with open('pathways', encoding='utf-8') as f:
            self.path = f.readline()

        self.path = self.path.strip('\n') + '//' + self.categories[0].strip('\n') + '//' + self.categories[0].strip('\n')

        with shelve.open(self.path) as f:
            self.count = len(f)

    def __uploadDataToTable(self):
        with shelve.open(self.path) as f:
            for num, index in enumerate(f):
                self.table.setItem(num, 0, QTableWidgetItem(index))
                self.table.setItem(num, 1, QTableWidgetItem(f[index]))

        self.table.move(0, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
