import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *


# from stacked_ui import Ui_Form
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(518, 277)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setMaximumSize(QtCore.QSize(100, 16777215))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("background:blue;")
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("background:red;")
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("background:yellow;")
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "Item  1"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "Item 2"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "Item 3"))
        self.listWidget.setSortingEnabled(__sortingEnabled)


class StackedExample(QWidget, Ui_Form):
    def __init__(self):
        super(StackedExample, self).__init__()
        self.setupUi(self)

        self.listWidget.currentRowChanged.connect(self.display)

    def display(self, row):
        self.stackedWidget.setCurrentIndex(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StackedExample()
    ex.show()
    sys.exit(app.exec_())