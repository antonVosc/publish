from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from datetime import datetime, timedelta
import random



class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(373, 256)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.colours=['red','green','black','orange','purple','blue','pink','white']
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(20, 0, 341, 21))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(150, 20, 41, 16))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(150, 40, 41, 16))
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(20, 60, 331, 141))
		font = QtGui.QFont()
		font.setPointSize(78)
		self.label_4.setFont(font)
		self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
		self.label_4.setObjectName("label_4")
		self.label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.text_colour = random.choice(self.colours)
		self.label_4.setStyleSheet('color: {}'.format(self.text_colour))
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(200, 20, 60, 16))
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(self.centralwidget)
		self.label_6.setGeometry(QtCore.QRect(200, 40, 31, 16))
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(self.centralwidget)
		self.label_7.setGeometry(QtCore.QRect(120, 70, 205, 16))
		self.label_7.setObjectName("label_7")
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(40, 180, 301, 31))
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit.returnPressed.connect(self.colour_check)
		MainWindow.setCentralWidget(self.centralwidget)
		self.start_show = 0
		self.score = 0
		self.left = 45
		self.total = 1
		self.time = QTimer()
		self.time.timeout.connect(self.timer)
		self.time.start(1000)
		self.word = random.choice(self.colours)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Colour quiz"))
		self.label.setText(_translate("MainWindow", "Type in the colours of the words, and not the word text!"))
		self.label_2.setText(_translate("MainWindow", "Score:"))
		self.label_3.setText(_translate("MainWindow", "Time:"))
		self.label_4.setText(_translate("MainWindow", self.word))
		self.label_5.setText(_translate("MainWindow", "0"))
		self.label_6.setText(_translate("MainWindow", "45"))
		self.label_7.setText(_translate("MainWindow", ""))


	def colour_check(self):
		if len(self.lineEdit.text())<3:
			self.label_7.setText('Your guess is wrong!')
			self.start_show = 3
		else:
			if self.lineEdit.text() == self.word and self.word != self.text_colour:
				self.start_show = 3
				self.label_7.setText('Type in the colour of the word, not the text itself!')
				self.update()
				self.total += 1
			elif self.lineEdit.text() == self.text_colour:
				self.score += 1
			self.update()
			self.total += 1


	def update(self):
		self.label_5.setText(str(self.score))
		self.lineEdit.setText('')
		self.text_colour = random.choice(self.colours)
		self.word = random.choice(self.colours)
		self.label_4.setStyleSheet('color: {}'.format(self.text_colour))
		self.label_4.setText(self.word)


	def timer(self):
		self.left -= 1
		if self.start_show == 0:
			self.label_7.setText('')
			self.start_show = 0
		if self.start_show > 0:
			self.start_show -=1
		self.label_6.setText(str(self.left))
		if self.left == -1:
			MainWindow.hide()
			end.show()
		self.text = "You managed to type "+str(self.score)+" correct colours out of "+str(self.total)+" in 45 seconds"
		end_ui.label.setText(self.text)


	def reset_ui(self):
		self.left = 45
		self.score = 0
		MainWindow.show()
		_translate = QtCore.QCoreApplication.translate
		self.label.setText(_translate("MainWindow", ''))
		self.label_2.setText(_translate("MainWindow", "Score:"))
		self.label_3.setText(_translate("MainWindow", "Time:"))
		self.lineEdit.setText('')
		self.text_colour = random.choice(self.colours)
		self.word = random.choice(self.colours)
		self.label_4.setStyleSheet('color: {}'.format(self.text_colour))
		self.label_4.setText(_translate("MainWindow", self.word))
		self.label_5.setText(_translate("MainWindow", "0"))
		self.label_6.setText(_translate("MainWindow", "45"))



class Ui_MainWindow1(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(235, 70)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(50, 40, 60, 17))
		self.pushButton.setObjectName("pushButton")
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(120, 40, 60, 17))
		self.pushButton_2.setObjectName("pushButton_2")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(7, 10, 240, 16))
		self.label.setObjectName("label")
		MainWindow.setCentralWidget(self.centralwidget)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.pushButton.clicked.connect(self.test)
		self.pushButton_2.clicked.connect(self.ext)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "End"))
		self.pushButton.setText(_translate("MainWindow", "Play Again"))
		self.pushButton_2.setText(_translate("MainWindow", "Exit"))
		self.label.setText(_translate("MainWindow", ''))


	def test(self):
		ui.reset_ui()


	def ext(self):
		sys.exit(app.exec_())
		sys.exit(app1.exec_())



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	app1 = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	end = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	end_ui = Ui_MainWindow1()
	end_ui.setupUi(end)
	MainWindow.show()
	end.hide()
	sys.exit(app.exec_())
	sys.exit(app1.exec_())
