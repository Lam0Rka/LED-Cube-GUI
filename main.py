from design import MainWindow
from Cube import Cube
from Falcon9 import launch
from tech_parser import shakalizator
from tech_parser import conversion
import sys
from PyQt5.Qt import QApplication, QMainWindow, QFileDialog
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
        self.ui.pushButton_cube_Load.clicked.connect(self.press_load)
        self.ui.pushButton_file_load.clicked.connect(self.press_load)
        self.ui.pushButton_open_cube.clicked.connect(self.open_cube)
        self.ui.pushButton_file_confirm.clicked.connect(self.press_confirm_file)
        self.ui.pushButton_file_open_file.clicked.connect(self.choose_file)

    def press_confirm(self, c: Cube, x, y, z, r, g, b) -> None:
        c.set_color(x, y, z, r, g, b)

    def press_load(self) -> None:
        file_name = QFileDialog.getOpenFileName(self)[0]
        
        try:
            self.file = open(file_name, 'w')
        except FileNotFoundError:
            print("File not found")

    def open_cube(self) -> None:
        launch()

    def choose_file(self) -> None:
        dialog = QFileDialog(self)
        dialog.setNameFilter("Json files (*.json)")

        self.file_name = dialog.getOpenFileName(self)[0]
        
        try:
            array = shakalizator.compression(self.file_name)

            # self.file = QFile(file_name)
        except FileNotFoundError:
            print("File not found")
        

    def press_confirm_file(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec())
