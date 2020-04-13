from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(299, 294)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
		self.lcdNumber.setGeometry(QtCore.QRect(10, 10, 271, 51))
		self.lcdNumber.setObjectName("lcdNumber")
		self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_7.setGeometry(QtCore.QRect(10, 70, 61, 41))
		self.pushButton_7.setObjectName("pushButton_7")
		self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_8.setGeometry(QtCore.QRect(80, 70, 61, 41))
		self.pushButton_8.setObjectName("pushButton_8")
		self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_9.setGeometry(QtCore.QRect(150, 70, 61, 41))
		self.pushButton_9.setObjectName("pushButton_9")
		self.divide_but = QtWidgets.QPushButton(self.centralwidget)
		self.divide_but.setGeometry(QtCore.QRect(220, 70, 61, 41))
		self.divide_but.setObjectName("divide")
		self.X = QtWidgets.QPushButton(self.centralwidget)
		self.X.setGeometry(QtCore.QRect(220, 120, 61, 41))
		self.X.setObjectName("X")
		self.minus_but = QtWidgets.QPushButton(self.centralwidget)
		self.minus_but.setGeometry(QtCore.QRect(220, 170, 61, 41))
		self.minus_but.setObjectName("minus")
		self.plus_but = QtWidgets.QPushButton(self.centralwidget)
		self.plus_but.setGeometry(QtCore.QRect(220, 220, 61, 41))
		self.plus_but.setObjectName("plus")
		self.result_but = QtWidgets.QPushButton(self.centralwidget)
		self.result_but.setGeometry(QtCore.QRect(150, 220, 61, 41))
		self.result_but.setObjectName("result")
		self.clear_but = QtWidgets.QPushButton(self.centralwidget)
		self.clear_but.setGeometry(QtCore.QRect(10, 220, 61, 41))
		self.clear_but.setObjectName("clear")
		self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_4.setGeometry(QtCore.QRect(10, 120, 61, 41))
		self.pushButton_4.setObjectName("pushButton_4")
		self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_5.setGeometry(QtCore.QRect(80, 120, 61, 40))
		self.pushButton_5.setObjectName("pushButton_5")
		self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_6.setGeometry(QtCore.QRect(150, 120, 61, 41))
		self.pushButton_6.setObjectName("pushButton_6")
		self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_1.setGeometry(QtCore.QRect(10, 170, 61, 41))
		self.pushButton_1.setObjectName("pushButton_1")
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(80, 170, 61, 41))
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setGeometry(QtCore.QRect(150, 170, 61, 41))
		self.pushButton_3.setObjectName("pushButton_3")
		self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_0.setGeometry(QtCore.QRect(80, 220, 61, 41))
		self.pushButton_0.setObjectName("pushButton_0")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 299, 18))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.pushButton_1.clicked.connect(self.button_1)
		self.pushButton_2.clicked.connect(self.button_2)
		self.pushButton_3.clicked.connect(self.button_3)
		self.pushButton_4.clicked.connect(self.button_4)
		self.pushButton_5.clicked.connect(self.button_5)
		self.pushButton_6.clicked.connect(self.button_6)
		self.pushButton_7.clicked.connect(self.button_7)
		self.pushButton_8.clicked.connect(self.button_8)
		self.pushButton_9.clicked.connect(self.button_9)
		self.pushButton_0.clicked.connect(self.button_0)
		self.divide_but.clicked.connect(self.divide)
		self.plus_but.clicked.connect(self.add)
		self.X.clicked.connect(self.multiply)
		self.minus_but.clicked.connect(self.minus)
		self.result_but.clicked.connect(self.equal)

		self.divided = False
		self.add = False
		self.multiply = False
		self.minus = False

		self.num = ""

	def button_1(self):
		self.num = self.num + "1"
		self.update_lcd(self.num)

	def button_2(self):
		self.num = self.num + "2"
		self.update_lcd(self.num)

	def button_3(self):
		self.num = self.num + "3"
		self.update_lcd(self.num)

	def button_4(self):
		self.num = self.num + "4"
		self.update_lcd(self.num)

	def button_5(self):
		self.num = self.num + "5"
		self.update_lcd(self.num)

	def button_6(self):
		self.num = self.num + "6"
		self.update_lcd(self.num)

	def button_7(self):
		self.num = self.num + "7"
		self.update_lcd(self.num)

	def button_8(self):
		self.num = self.num + "8"
		self.update_lcd(self.num)

	def button_9(self):
		self.num = self.num + "9"
		self.update_lcd(self.num)

	def button_0(self):
		self.num = self.num + "0"
		self.update_lcd(self.num)

	def divide(self):
		global first_num,result
		self.divided = True
		try:
			self.first_num = int(self.num)
		except ValueError:
			pass
		self.num = ''

	def add(self):
		global first_num,result
		self.add = True
		try:
			self.first_num = int(self.num)
		except ValueError:
			pass
		self.num = ''

	def multiply(self):
		global first_num,result
		self.multiply = True
		try:
			self.first_num = int(self.num)
		except ValueError:
			pass
		self.num = ''

	def minus(self):
		global first_num,result
		self.minus = True
		try:
			self.first_num = int(self.num)
		except ValueError:
			pass
		self.num = ''


	def equal(self):
		try:
			self.second_num=int(self.num)
			self.update_lcd(self.num)

			if self.divided == True:
				self.result=self.first_num / self.second_num
				self.divided = False

			if self.add == True:
				self.result=self.first_num + self.second_num
				self.add = False

			if self.multiply == True:
				self.result=self.first_num * self.second_num
				self.multiply = False

			if self.minus == True:
				self.result=self.first_num - self.second_num
				self.minus = False

			self.update_lcd(str(self.result))
		except ValueError:
			pass

		self.num = ''
		self.first_num = ''
		self.result = 0


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton_7.setText(_translate("MainWindow", "7"))
		self.pushButton_8.setText(_translate("MainWindow", "8"))
		self.pushButton_9.setText(_translate("MainWindow", "9"))
		self.divide_but.setText(_translate("MainWindow", "/"))
		self.X.setText(_translate("MainWindow", "X"))
		self.minus_but.setText(_translate("MainWindow", "-"))
		self.plus_but.setText(_translate("MainWindow", "+"))
		self.result_but.setText(_translate("MainWindow", "="))
		self.clear_but.setText(_translate("MainWindow", "C"))
		self.pushButton_4.setText(_translate("MainWindow", "4"))
		self.pushButton_5.setText(_translate("MainWindow", "5"))
		self.pushButton_6.setText(_translate("MainWindow", "6"))
		self.pushButton_1.setText(_translate("MainWindow", "1"))
		self.pushButton_2.setText(_translate("MainWindow", "2"))
		self.pushButton_3.setText(_translate("MainWindow", "3"))
		self.pushButton_0.setText(_translate("MainWindow", "0"))

	def update_lcd(self,button):
		self.lcdNumber.display(button)




if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
