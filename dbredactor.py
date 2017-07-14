import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QMessageBox,\
    QTableWidgetItem, QVBoxLayout, QPushButton, QHBoxLayout, QTextEdit, QLabel, QComboBox
import shelve


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Редагування бази даних')
        self.resize(1100, 300)
        self.mainLayout = QHBoxLayout()
        self.path = None
        self.categories = []

        self.titles = ['Голосні', 'Приголосні', 'Глухі приголосні',
                       'Пробіл', '"Інші букви"', 'Подвоєння', '"Або"', 'Будь-який символ', 'Цифра', 'Крапка',
                       'Межа слова', 'Межа слова \n-Або-\n Межа слова']

        self.commandsArray = ['[аеєиіїоуюя]', '[бвгґджзйклмнпрстфхцчшщ]', '[пхктшчсц]',
                              '\\s', '\\w+', '{2}', '|', '.', '[0-9]', '\.', '\\b', '\\b|\\b']

        self.currentSimbol = None

        self.__loadCategories()
        self.__createTable()
        self.__createTextFilds()
        self.__createButtons()

        self.setLayout(self.mainLayout)
        self.show()

    def __createTable(self):
        layout1 = QHBoxLayout()
        self.box = QComboBox()

        self.box.addItems(self.categories)

        loadButton = QPushButton('Завантажити')
        loadButton.clicked.connect(lambda: self.__uploadDataToTable(self.box.currentText()))

        layout1.addWidget(self.box)
        layout1.addWidget(loadButton)

        self.table = QTableWidget()
        layout2 = QVBoxLayout()
        layout2.addLayout(layout1)
        layout2.addWidget(self.table)

        self.mainLayout.addLayout(layout2)

    def __createTextFilds(self):
        lab1 = QLabel('Шаблон пошуку')
        lab2 = QLabel('Коментар')

        self.patternArea = QTextEdit()
        self.hintArea = QTextEdit()

        self.correctButton = QPushButton('Редагувати')
        self.correctButton.clicked.connect(lambda: self.__updateDataInDB())
        self.deleteButton = QPushButton('Видалити')
        self.deleteButton.clicked.connect(lambda: self.__deleteFromDB())
        self.cancelButton = QPushButton('Відмінити')

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.correctButton)
        buttonLayout.addWidget(self.deleteButton)
        buttonLayout.addWidget(self.cancelButton)

        layout = QVBoxLayout()
        layout.addWidget(lab1)
        layout.addWidget(self.patternArea)
        layout.addWidget(lab2)
        layout.addWidget(self.hintArea)
        layout.addLayout(buttonLayout)
        self.mainLayout.addLayout(layout)

    def __createButtons(self):
        layout = QVBoxLayout()

        for index, value in enumerate(self.titles):
            butt = QPushButton(value)
            butt.clicked.connect(lambda x, y=self.commandsArray[index].strip('\n'): self.__takeStrings(y))
            layout.addWidget(butt)

        self.mainLayout.addLayout(layout)

    def __takeStrings(self, mark):
        self.patternArea.insertPlainText(mark)

    def __loadCategories(self):
        with open('categoryes', encoding='utf-8') as f:
            for value in f:
                self.categories.append(value)

    def __loadData(self, endOfPath):
        with open('pathways', encoding='utf-8') as f:
            self.path = f.readline()

        self.path = self.path.strip('\n') + '//' + endOfPath.strip('\n') + '//' + endOfPath.strip('\n')

        f = None
        try:
            f = shelve.open(self.path)
            self.count = len(f)
        except Exception:
            self.table.clear()
        finally:
            if f is not None:
                f.close()

    def __uploadDataToTable(self, endOfPath):
        self.__loadData(endOfPath)

        self.table.setColumnCount(2)
        self.table.setRowCount(self.count)

        if self.count == 0:
            QMessageBox.information(self, 'Інфо', 'База порожня')

        f = None
        try:
            f = shelve.open(self.path)

            for num, index in enumerate(f):
                self.table.setItem(num, 0, QTableWidgetItem(index))
                self.table.setItem(num, 1, QTableWidgetItem(f[index]))
        except Exception:
            self.table.clear()
        finally:
            if f is not None:
                f.close()

        self.table.setHorizontalHeaderLabels(('Шаблон', 'Коментар'))
        self.table.itemClicked.connect(lambda: self.__setDataToAreas())

    def __setDataToAreas(self):
        for i in self.table.selectedItems():
            if i.column() == 0:
                self.patternArea.clear()
                self.patternArea.append(i.text())
                self.currentSimbol = i.text()
                self.hintArea.clear()
                self.hintArea.append(self.table.item(i.row(), (i.column()+1)).text())

    def __deleteFromDB(self, updateFlag=False):
        print(self.currentSimbol)
        if self.path is not None and self.currentSimbol is not None:
            print('is not None', self.currentSimbol)
            f = None
            try:
                f = shelve.open(self.path)
                del f[self.currentSimbol]
                self.__uploadDataToTable(self.box.currentText())
                self.patternArea.clear()
                self.hintArea.clear()
            except Exception:
                self.table.clear()
            finally:
                if f is not None:
                    f.close()
                self.currentSimbol = None
        elif not updateFlag:
            QMessageBox.information(self, 'Помилка роботи з базою', 'Завантажте базу або оберіть шаблон для роботи')

    def __updateDataInDB(self):
        if self.path is not None and self.currentSimbol is not None:
            try:
                f = shelve.open(self.path)
                print(f)
                f[self.patternArea.toPlainText().lower()] = self.hintArea.toPlainText()
                self.__uploadDataToTable(self.box.currentText())

                if self.currentSimbol != self.patternArea.toPlainText():
                    self.__deleteFromDB(True)

                self.patternArea.clear()
                self.hintArea.clear()
            except Exception:
                print('exception in __updateDataInDB')
            finally:
                if f is not None:
                    f.close()
                self.currentSimbol = None
        else:
            QMessageBox.information(self, 'Помилка роботи з базою', 'Завантажте базу або оберіть шаблон для роботи')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
