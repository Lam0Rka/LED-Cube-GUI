import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 650)

        max_num_color = QRegExp("(0*(?:[0-9][0-9]?|[0-2][0-5][0-5]))")
        max_num_coord = QRegExp("[0-7]")

        #central виджет
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1100, 650))
        self.tabWidget.setObjectName("tabWidget")

        #Всё, что относится к вкладке "Cube"
        self.tab_cube = QtWidgets.QWidget()
        self.tab_cube.setObjectName("tab_cube")

        self.openGLWidget = QtWidgets.QOpenGLWidget(self.tab_cube)
        self.openGLWidget.setGeometry(QtCore.QRect(300, 0, 791, 601))
        self.openGLWidget.setObjectName("openGLWidget")

        self.lineEdit_X = QtWidgets.QLineEdit(self.tab_cube)
        self.lineEdit_X.setGeometry(QtCore.QRect(60, 140, 41, 41))
        self.lineEdit_X.setObjectName("Edit_X")
        self.lineEdit_X.setFont(QFont('Arial', 14))
        input_validator = QRegExpValidator(max_num_coord, self.lineEdit_X)
        self.lineEdit_X.setValidator(input_validator)


        self.lineEdit_Y = QtWidgets.QLineEdit(self.tab_cube)
        self.lineEdit_Y.setGeometry(QtCore.QRect(120, 140, 41, 41))
        self.lineEdit_Y.setObjectName("lineEdit_Y")
        self.lineEdit_Y.setFont(QFont('Arial', 14))
        input_validator = QRegExpValidator(max_num_coord, self.lineEdit_Y)
        self.lineEdit_Y.setValidator(input_validator)

        self.lineEdit_Z = QtWidgets.QLineEdit(self.tab_cube)
        self.lineEdit_Z.setGeometry(QtCore.QRect(180, 140, 41, 41))
        self.lineEdit_Z.setObjectName("lineEdit_Z")
        self.lineEdit_Z.setFont(QFont('Arial', 14))
        input_validator = QRegExpValidator(max_num_coord, self.lineEdit_Z)
        self.lineEdit_Z.setValidator(input_validator)

        self.lineEdit_R = QtWidgets.QLineEdit(self.tab_cube)
        self.lineEdit_R.setGeometry(QtCore.QRect(60, 300, 41, 41))
        self.lineEdit_R.setObjectName("Edit_R")
        self.lineEdit_R.setFont(QFont('Arial', 14))
        input_validator = QRegExpValidator(max_num_color, self.lineEdit_R)
        self.lineEdit_R.setValidator(input_validator)

        self.lineEdit_G = QtWidgets.QLineEdit(self.tab_cube)
        self.lineEdit_G.setGeometry(QtCore.QRect(120, 300, 41, 41))
        self.lineEdit_G.setObjectName("lineEdit_G")
        self.lineEdit_G.setFont(QFont('Arial', 14))
        input_validator = QRegExpValidator(max_num_color, self.lineEdit_G)
        self.lineEdit_G.setValidator(input_validator)

        self.lineEdit_B = QtWidgets.QLineEdit(self.tab_cube)
        self.lineEdit_B.setGeometry(QtCore.QRect(180, 300, 41, 41))
        self.lineEdit_B.setObjectName("lineEdit_B")
        self.lineEdit_B.setFont(QFont('Arial', 14))
        input_validator = QRegExpValidator(max_num_color, self.lineEdit_B)
        self.lineEdit_B.setValidator(input_validator)


        self.pushButton_cube_Load = QtWidgets.QPushButton(self.tab_cube)
        self.pushButton_cube_Load.setGeometry(QtCore.QRect(60, 430, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_cube_Load.setFont(font)
        self.pushButton_cube_Load.setObjectName("pushButton_cube_Load")

        self.pushButton_cube_confirm = QtWidgets.QPushButton(self.tab_cube)
        self.pushButton_cube_confirm.setGeometry(QtCore.QRect(60, 370, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_cube_confirm.setFont(font)
        self.pushButton_cube_confirm.setObjectName("pushButton_cube_confirm")

        self.pushButton_open_cube = QtWidgets.QPushButton(self.tab_cube)
        self.pushButton_open_cube.setGeometry(QtCore.QRect(60, 490, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_open_cube.setFont(font)
        self.pushButton_open_cube.setObjectName("pushButton_open_cube")

        self.label_coordinates = QtWidgets.QLabel(self.tab_cube)
        self.label_coordinates.setGeometry(QtCore.QRect(60, 50, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_coordinates.setFont(font)
        self.label_coordinates.setAlignment(QtCore.Qt.AlignCenter)
        self.label_coordinates.setObjectName("label_coordinates")

        self.label_color = QtWidgets.QLabel(self.tab_cube)
        self.label_color.setEnabled(True)
        self.label_color.setGeometry(QtCore.QRect(100, 210, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_color.setFont(font)
        self.label_color.setObjectName("label_color")


        self.label_X = QtWidgets.QLabel(self.tab_cube)
        self.label_X.setGeometry(QtCore.QRect(70, 100, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_X.setFont(font)
        self.label_X.setObjectName("label_X")
        self.label_X.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y = QtWidgets.QLabel(self.tab_cube)
        self.label_Y.setGeometry(QtCore.QRect(130, 100, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_Y.setFont(font)
        self.label_Y.setObjectName("label_Y")
        self.label_Y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Z = QtWidgets.QLabel(self.tab_cube)
        self.label_Z.setGeometry(QtCore.QRect(190, 100, 20, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_Z.setFont(font)
        self.label_Z.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Z.setObjectName("label_Z")

        self.label_R = QtWidgets.QLabel(self.tab_cube)
        self.label_R.setGeometry(QtCore.QRect(70, 260, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_R.setFont(font)
        self.label_R.setAlignment(QtCore.Qt.AlignCenter)
        self.label_R.setObjectName("label_R")

        self.label_G = QtWidgets.QLabel(self.tab_cube)
        self.label_G.setGeometry(QtCore.QRect(130, 260, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_G.setFont(font)
        self.label_G.setAlignment(QtCore.Qt.AlignCenter)
        self.label_G.setObjectName("label_G")

        self.label_B = QtWidgets.QLabel(self.tab_cube)
        self.label_B.setGeometry(QtCore.QRect(190, 260, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_B.setFont(font)
        self.label_B.setAlignment(QtCore.Qt.AlignCenter)
        self.label_B.setObjectName("label_B")


        #Всё, что относится к вкладке "file"
        self.tabWidget.addTab(self.tab_cube, "")
        self.tab_file = QtWidgets.QWidget()
        self.tab_file.setObjectName("tab_file")

        self.label_choose_file = QtWidgets.QLabel(self.tab_file)
        self.label_choose_file.setGeometry(QtCore.QRect(60, 50, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_choose_file.setFont(font)
        self.label_choose_file.setObjectName("label_choose_file")

        self.pushButton_file_load = QtWidgets.QPushButton(self.tab_file)
        self.pushButton_file_load.setGeometry(QtCore.QRect(220, 190, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_file_load.setFont(font)
        self.pushButton_file_load.setObjectName("pushButton_file_load")

        self.pushButton_file_confirm = QtWidgets.QPushButton(self.tab_file)
        self.pushButton_file_confirm.setGeometry(QtCore.QRect(50, 190, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_file_confirm.setFont(font)
        self.pushButton_file_confirm.setObjectName("pushButton_confirm")

        self.pushButton_file_open_file = QtWidgets.QPushButton(self.tab_file)
        self.pushButton_file_open_file.setGeometry(QtCore.QRect(50, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_file_open_file.setFont(font)
        self.pushButton_file_open_file.setObjectName("pushButton_file_open_file")

        #Всё, что относится к вкладке "Layers"
        self.tabWidget.addTab(self.tab_file, "")
        self.tab_layers = QtWidgets.QWidget()
        self.tab_layers.setObjectName("tab_layers")
        self.tabWidget.addTab(self.tab_layers, "")

        #Что-то ещё
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton_cube_Load.setText(_translate("MainWindow", "Load"))
        self.pushButton_cube_confirm.setText(_translate("MainWindow", "Confirm"))
        self.pushButton_open_cube.setText(_translate("MainWindow", "Open cube"))

        self.label_coordinates.setText(_translate("MainWindow", "Coordinates"))
        self.label_color.setText(_translate("MainWindow", "Color"))
        self.label_X.setText(_translate("MainWindow", "X"))
        self.label_Y.setText(_translate("MainWindow", "Y"))
        self.label_Z.setText(_translate("MainWindow", "Z"))
        self.label_R.setText(_translate("MainWindow", "R"))
        self.label_G.setText(_translate("MainWindow", "G"))
        self.label_B.setText(_translate("MainWindow", "B"))

        self.label_choose_file.setText(_translate("MainWindow", "Choose file_name.obj"))
        self.pushButton_file_load.setText(_translate("MainWindow", "Load"))
        self.pushButton_file_confirm.setText(_translate("MainWindow", "Confirm"))
        self.pushButton_file_open_file.setText(_translate("MainWindow", "Open File"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cube), _translate("MainWindow", "Cube"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_file), _translate("MainWindow", "File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_layers), _translate("MainWindow", "Layers"))


