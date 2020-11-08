from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from stegano import lsb
import os

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(658, 536)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(50, 130, 501, 20))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.lineEdit.setFont(font)
		self.lineEdit.setObjectName("lineEdit")
		self.Encrypt_browse = QtWidgets.QPushButton(self.centralwidget)
		self.Encrypt_browse.setGeometry(QtCore.QRect(560, 130, 56, 21))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.Encrypt_browse.setFont(font)
		self.Encrypt_browse.setObjectName("Encrypt_browse")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(180, 20, 341, 31))
		font = QtGui.QFont()
		font.setPointSize(24)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(320, 50, 171, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(50, 180, 501, 20))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.lineEdit_2.setFont(font)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.Save = QtWidgets.QPushButton(self.centralwidget)
		self.Save.setGeometry(QtCore.QRect(560, 180, 56, 21))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.Save.setFont(font)
		self.Save.setObjectName("Save")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(50, 110, 211, 16))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(50, 160, 231, 16))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(50, 210, 35, 10))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")
		self.status_label = QtWidgets.QLabel(self.centralwidget)
		self.status_label.setGeometry(QtCore.QRect(60, 230, 491, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.status_label.setFont(font)
		self.status_label.setObjectName("status_label")
		self.label_7 = QtWidgets.QLabel(self.centralwidget)
		self.label_7.setGeometry(QtCore.QRect(290, 80, 141, 21))
		font = QtGui.QFont()
		font.setPointSize(16)
		font.setBold(True)
		font.setWeight(75)
		self.label_7.setFont(font)
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(self.centralwidget)
		self.label_8.setGeometry(QtCore.QRect(290, 270, 141, 21))
		font = QtGui.QFont()
		font.setPointSize(16)
		font.setBold(True)
		font.setWeight(75)
		self.label_8.setFont(font)
		self.label_8.setObjectName("label_8")
		self.Decrypt_browse = QtWidgets.QPushButton(self.centralwidget)
		self.Decrypt_browse.setGeometry(QtCore.QRect(560, 320, 56, 21))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.Decrypt_browse.setFont(font)
		self.Decrypt_browse.setObjectName("Decrypt_browse")
		self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_3.setGeometry(QtCore.QRect(50, 320, 501, 20))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.lineEdit_3.setFont(font)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.label_9 = QtWidgets.QLabel(self.centralwidget)
		self.label_9.setGeometry(QtCore.QRect(50, 300, 211, 16))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_9.setFont(font)
		self.label_9.setObjectName("label_9")
		self.label_10 = QtWidgets.QLabel(self.centralwidget)
		self.label_10.setGeometry(QtCore.QRect(50, 360, 111, 16))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_10.setFont(font)
		self.label_10.setObjectName("label_10")
		self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
		self.textBrowser.setGeometry(QtCore.QRect(50, 390, 561, 111))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.textBrowser.setFont(font)
		self.textBrowser.setObjectName("textBrowser")
		MainWindow.setCentralWidget(self.centralwidget)

		self.Encrypt_browse.clicked.connect(self.choose_path)
		self.Save.clicked.connect(self.encrypt_message)
		self.Decrypt_browse.clicked.connect(self.decrypt_message)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Secret Message Encoder"))
		self.Encrypt_browse.setText(_translate("MainWindow", "Browse"))
		self.label.setText(_translate("MainWindow", "Secret message encoder"))
		self.label_2.setText(_translate("MainWindow", "Developed by Anton Voshchinskiy"))
		self.Save.setText(_translate("MainWindow", "Save"))
		self.label_3.setText(_translate("MainWindow", "Please select image to encrypt:"))
		self.label_4.setText(_translate("MainWindow", "Please enter text to secret message:"))
		self.label_5.setText(_translate("MainWindow", "Status:"))
		self.status_label.setText(_translate("MainWindow", "No file selected, please select file"))
		self.label_7.setText(_translate("MainWindow", "Encrypt"))
		self.label_8.setText(_translate("MainWindow", "Decrypt"))
		self.Decrypt_browse.setText(_translate("MainWindow", "Browse"))
		self.label_9.setText(_translate("MainWindow", "Please select image to decrypt:"))
		self.label_10.setText(_translate("MainWindow", "Secret message:"))

	def choose_path(self):
		self.fileName = QtWidgets.QFileDialog.getOpenFileName(None, "Please Select File", "", "Image Files (*.png)")
		self.lineEdit.setText(self.fileName[0])
		if self.lineEdit.text() != '':
			self.status_label.setText('File selected. Please enter a secret message')

	def encrypt_message(self):
		try:
			encrypt = lsb.hide(self.fileName[0],self.lineEdit_2.text())
			encrypt.save(self.fileName[0])
			self.status_label.setText('The secret message is encrypted and the file is saved')
			msg = QMessageBox()
			msg.setWindowTitle('File saved')
			msg.setText('The file has been saved.')
			msg.exec_()
		except (AttributeError, AssertionError) as e:
			msg = QMessageBox()
			msg.setWindowTitle('Error')
			msg.setText('Please enter the message')
			msg.exec_()

	def decrypt_message(self):
		try:
			self.fileName = QtWidgets.QFileDialog.getOpenFileName(None, "Please Select File", "", "Image Files (*.png)")
			self.lineEdit_3.setText(self.fileName[0])
			clear_message = lsb.reveal(self.fileName[0])
			self.textBrowser.setText(clear_message)
			self.status_label.setText('Your secret message has been decrypted')
		except AttributeError as e:
			msg = QMessageBox()
			msg.setWindowTitle('Error')
			msg.setText('Please select the picture')
			msg.exec_()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())