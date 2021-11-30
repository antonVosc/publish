from PyQt5 import QtCore, QtGui, QtWidgets
import cv2, qrcode

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.PhotoBox = QtWidgets.QLabel(self.centralwidget)
        self.PhotoBox.setGeometry(QtCore.QRect(10, 10, 200, 200))
        self.PhotoBox.setFrameShape(QtWidgets.QFrame.Box)
        self.PhotoBox.setText("")
        self.PhotoBox.setObjectName("PhotoBox")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 5, 175, 210))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 240, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 250, 191))
        self.label.setText("")
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 230, 381, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 240, 251, 161))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 10, 191, 200))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.read_qr)
        self.pushButton_2.clicked.connect(self.to_qr)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QR codes"))
        self.pushButton.setText(_translate("MainWindow", "Convert to text"))
        self.pushButton_2.setText(_translate("MainWindow", "Convert to QR"))

    def read_qr(self):
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(None, "Please Select File", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if self.fileName is not None:
            pixmap = QtGui.QPixmap(self.fileName[0])
            pixmap = pixmap.scaled(self.PhotoBox.width(), self.PhotoBox.height(),QtCore.Qt.KeepAspectRatio)
            self.PhotoBox.setPixmap(pixmap)
        img = cv2.imread(self.fileName[0])
        detection = cv2.QRCodeDetector()
        val, pts, st_code = detection.detectAndDecode(img)
        self.lineEdit_2.setText(val)

    def to_qr(self):
        img = qrcode.make(self.lineEdit.text())
        img.save('QR.png')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
