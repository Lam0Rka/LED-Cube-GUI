from design import MainWindow
from Cube import Cube
import sys
from PyQt5.Qt import QApplication, QMainWindow
from PyQt5.QtGui import QFontDatabase
from PyQt5 import QtOpenGL

cube = Cube()


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

        self.ui.pushButton_cube_confirm.clicked.connect(
            lambda: self.press_confirm(cube, int(self.ui.lineEdit_X), int(self.ui.lineEdit_Y), int(self.ui.lineEdit_Z),
                                       int(self.ui.lineEdit_R), int(self.ui.lineEdit_G), int(self.ui.lineEdit_B)))
        self.ui.pushButton_cube_Load.clicked.connect(lambda: self.press_load())
        self.ui.pushButton_file_load.clicked.connect(lambda: self.press_load())
        self.ui.pushButton_file_confirm.clicked.connect(lambda: self.press_confirm_file())
        self.ui.pushButton_file_open_file.clicked.connect(lambda: self.choose_file())

    def press_confirm(self, c: Cube, x, y, z, r, g, b) -> None:
        c.set_color(x, y, z, r, g, b)

    def press_load(self) -> None:
        pass

    def choose_file(self) -> None:
        pass

    def press_confirm_file(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec())
