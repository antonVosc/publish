# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Countdown(object):
    def setupUi(self, Countdown):
        Countdown.setObjectName("Countdown")
        Countdown.resize(455, 444)
        self.centralwidget = QtWidgets.QWidget(Countdown)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(11, 30, 431, 171))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(10, 240, 431, 171))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        Countdown.setCentralWidget(self.centralwidget)

        self.retranslateUi(Countdown)
        QtCore.QMetaObject.connectSlotsByName(Countdown)

    def retranslateUi(self, Countdown):
        _translate = QtCore.QCoreApplication.translate
        Countdown.setWindowTitle(_translate("Countdown", "MainWindow"))
        self.label.setText(_translate("Countdown", "Days:"))
        self.label_2.setText(_translate("Countdown", "Hours:"))


if __name__ == "__main__":
    import sys
    app1 = QtWidgets.QApplication(sys.argv)
    Countdown = QtWidgets.QMainWindow()
    ui1 = Ui_Countdown()
    ui1.setupUi(Countdown)
    Countdown.show()
    sys.exit(app1.exec_())
