from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from datetime import datetime, timedelta


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(218, 259)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
		self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 200, 144))
		self.calendarWidget.setObjectName("calendarWidget")
		self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
		self.timeEdit.setGeometry(QtCore.QRect(10, 160, 201, 51))
		font = QtGui.QFont()
		font.setPointSize(20)
		self.timeEdit.setFont(font)
		self.timeEdit.setObjectName("timeEdit")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(10, 220, 201, 31))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		MainWindow.setCentralWidget(self.centralwidget)
		self.pushButton.clicked.connect(self.get_info)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "Start cuntdown"))


	def get_info(self):
		self.date = self.calendarWidget.selectedDate()
		self.date = self.date.toString("dd/MM/yyyy")
		self.full_date = self.date+' '+self.timeEdit.time().toString()
		self.datetime_object = datetime.strptime(self.full_date, '%d/%m/%Y %H:%M:%S')
		self.now = datetime.now()
		self.left = self.datetime_object - self.now
		MainWindow.hide()
		Countdown.show()
		ui1.start_timer(self.left)


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
		self.flag =  False
		self.left = 0
		self.timer = QTimer()
		self.timer.timeout.connect(self.str_time)
		self.timer.start(1000)


	def retranslateUi(self, Countdown):
		_translate = QtCore.QCoreApplication.translate
		Countdown.setWindowTitle(_translate("Countdown", "MainWindow"))
		self.label.setText(_translate("Countdown", "Days:"))
		self.label_2.setText(_translate("Countdown", "Hours:"))


	def str_time(self):
		if self.left != 0:
			self.left = self.left - timedelta(seconds=1)
			self.display_time()


	def start_timer(self,left):
		self.left = left


	def display_time(self):
		self.ct = str(self.left)
		self.days=''
		spaces = 0
		i = 0
		if ' ' in self.ct:
			while self.ct[i]!=' ':
				self.days+=self.ct[i]
				i+=1
		else:
			self.days = 0

		self.full_time=''
		self.time=''
		g=0
		while g!=len(self.ct):
			if self.ct[g]==' ':
				spaces=spaces+1
			elif spaces>1 or ' ' not in self.ct:
				self.full_time=self.full_time+self.ct[g]
			g=g+1

		point=0
		g=0
		while g!=len(self.full_time):
			if self.full_time[g]=='.':
				point=point+1
			elif point<1:
				self.time=self.time+self.full_time[g]
			g=g+1

		self.lcdNumber.display(self.days)
		self.lcdNumber_2.setDigitCount(len(self.time))
		self.lcdNumber_2.display(self.time)


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	app1 = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	Countdown = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui1 = Ui_Countdown()
	ui1.setupUi(Countdown)
	MainWindow.show()
	Countdown.hide()
	sys.exit(app.exec_())
	sys.exit(app1.exec_())
