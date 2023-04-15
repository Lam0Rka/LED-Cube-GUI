from design import MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *


class Example(QWidget, MainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.setupUi(self)

        self.listWidget.currentRowChanged.connect(self.display)

    def display(self, row):
        self.stackedWidget.setCurrentIndex(row)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()