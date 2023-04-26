
from design import MainWindow
import sys
from PyQt5.Qt import QApplication, QMainWindow
from PyQt5.QtGui import QFontDatabase
from PyQt5 import QtOpenGL


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    window.show()

    sys.exit(app.exec())
