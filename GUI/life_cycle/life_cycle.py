from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from datetime import datetime
from win32api import GetSystemMetrics
import arcade,pyautogui
import tkinter as tk
from tkinter import filedialog

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(221, 193)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
		self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 200, 144))
		self.calendarWidget.setObjectName("calendarWidget")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(10, 160, 91, 21))
		self.pushButton.setObjectName("pushButton")
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(110, 160, 101, 20))
		self.pushButton_2.setObjectName("pushButton_2")
		MainWindow.setCentralWidget(self.centralwidget)
		self.weeks = 0
		self.pushButton.clicked.connect(self.get_date)
		self.pushButton_2.clicked.connect(self.screenshot)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "Show"))
		self.pushButton_2.setText(_translate("MainWindow", "Save"))


	def win(self):
		self.width = GetSystemMetrics(0)
		self.height = GetSystemMetrics(1)
		self.gap = 24
		arcade.open_window(self.width,self.height,"Life cycle") #open
		arcade.set_background_color((255,255,255,5)) #back colour
		arcade.start_render() #colour in
		arcade.draw_text("You have lived:", self.width/2.4, self.height/60*57, arcade.color.BLACK, 70)
		self.start_y = 47*(self.height/50)
		self.colored = 0
		for g in range(81):
			self.start_x = self.width/3
			for i in range(52):
				if self.colored<self.weeks:
					arcade.draw_circle_filled(self.start_x,self.start_y,8,arcade.color.RED)
					self.colored += 1
				else:
					arcade.draw_circle_outline(self.start_x,self.start_y,8,arcade.color.BLACK)
				self.start_x += self.gap
			self.start_y -= self.gap
			arcade.finish_render() #stop colouring
		arcade.run() #execute


	def get_date(self):
		self.date = self.calendarWidget.selectedDate()
		self.date = self.date.toString("dd/MM/yyyy")
		self.time = "0:0:0"
		self.full_date = self.date+' '+self.time
		self.date_time_obj = datetime.strptime(self.full_date, '%d/%m/%Y %H:%M:%S')
		self.curr_date_time = datetime.now()
		self.left = self.date_time_obj - self.curr_date_time
		self.left=str(self.left)
		self.days=''
		g=0
		while self.left[g]!=' ':
			self.days += self.left[g]
			g=g+1
		self.days=int(self.days)
		self.weeks = (self.days//7)*-1
		self.win()

	def screenshot(self):
		self.get_date()
		screensh = pyautogui.screenshot()
		file_path = filedialog.asksaveasfilename(defaultextension='.png')
		screensh.save(file_path)


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
