from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider
from PIL import Image, ImageFilter

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SelectPhotos = QtWidgets.QPushButton(self.centralwidget)
        self.SelectPhotos.setGeometry(QtCore.QRect(515, 10, 61, 500))
        self.SelectPhotos.setObjectName("SelectPhotos")
        self.PhotoBox = QtWidgets.QLabel(self.centralwidget)
        self.PhotoBox.setGeometry(QtCore.QRect(10, 10, 500, 500))
        self.PhotoBox.setFrameShape(QtWidgets.QFrame.Box)
        self.PhotoBox.setText("")
        self.PhotoBox.setObjectName("PhotoBox")
        self.effect_button = QtWidgets.QPushButton(self.centralwidget)
        self.effect_button.setGeometry(QtCore.QRect(480, 512, 100, 17))
        self.effect_button.setObjectName("Effect_button")
        self.blur_effect_button = QtWidgets.QPushButton(self.centralwidget)
        self.blur_effect_button.setGeometry(QtCore.QRect(375, 512, 100, 17))
        self.blur_effect_button.setObjectName("BlurEffect_button")
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 520, 160, 16))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(5)
        MainWindow.setCentralWidget(self.centralwidget)


        self.SelectPhotos.clicked.connect(self.select)
        self.effect_button.clicked.connect(self.effect)
        self.blur_effect_button.clicked.connect(self.blur)
        self.horizontalSlider.sliderReleased.connect(self.valuechange)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SelectPhotos.setText(_translate("MainWindow", "Select photos"))
        self.effect_button.setText(_translate("MainWindow", "Black and white effect"))
        self.blur_effect_button.setText(_translate("MainWindow", "Blur effect"))

    def select(self):
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(None, "Please Select File", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if self.fileName is not None:
            pixmap = QtGui.QPixmap(self.fileName[0])
            pixmap = pixmap.scaled(self.PhotoBox.width(), self.PhotoBox.height(),QtCore.Qt.KeepAspectRatio)
            self.PhotoBox.setPixmap(pixmap)

    def effect(self):
        image = Image.open(self.fileName[0])
        image  = image.convert('L')
        image.save('temp.jpeg')
        pixmap = QtGui.QPixmap('temp.jpeg')
        pixmap = pixmap.scaled(self.PhotoBox.width(), self.PhotoBox.height(),QtCore.Qt.KeepAspectRatio)
        self.PhotoBox.setPixmap(pixmap)

    def blur(self):
        image = Image.open(self.fileName[0])
        self.size = self.horizontalSlider.value()
        image = image.filter(ImageFilter.GaussianBlur(self.size))
        image.save('temp.jpeg')
        pixmap = QtGui.QPixmap('temp.jpeg')
        pixmap = pixmap.scaled(self.PhotoBox.width(), self.PhotoBox.height(),QtCore.Qt.KeepAspectRatio)
        self.PhotoBox.setPixmap(pixmap)

    def valuechange(self):
        self.blur()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
