from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os,requests,shutil
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QLabel,QMessageBox
from PyQt5.QtGui import QIcon, QPixmap

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 545)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 35, 10))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 721, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 771, 351))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(740, 20, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 691, 441))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(705, 480, 91, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.load)
        self.pushButton_2.clicked.connect(self.save)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Link:"))
        self.pushButton.setText(_translate("MainWindow", "Load"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", "Save as..."))


    def save(self):
        self.url = self.lineEdit.text()
        try:
            self.r = requests.get(self.url,stream = True)
            self.r.raw.decode_content = True
            self.filename = QFileDialog.getSaveFileName(self, 'Save file',
             'c:\\',"Image files (*.jpg *.gif)")
            with open(self.filename[0],'wb') as f:
                shutil.copyfileobj(self.r.raw,f)
        except requests.exceptions.MissingSchema:
                mes = QMessageBox()
                mes.setText('Invalid URL!')
                mes.exec_()


    def load(self):
        self.url = self.lineEdit.text()
        self.filename = 'temp\\temp'
        try:
            self.r = requests.get(self.url,stream = True)
            self.r.raw.decode_content = True
            with open(self.filename,'wb') as f:
                shutil.copyfileobj(self.r.raw,f)
                pixmap = QtGui.QPixmap(self.filename)
                pixmap = pixmap.scaled(self.label_3.width(), self.label_3.height(),QtCore.Qt.KeepAspectRatio)
                self.label_3.setPixmap(pixmap)
            os.remove(self.filename)
        except requests.exceptions.MissingSchema:
            mes = QMessageBox()
            mes.setText('Invalid URL!')
            mes.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
