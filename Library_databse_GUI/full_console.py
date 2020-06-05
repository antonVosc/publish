from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QTableWidget,QTableWidgetItem
import sqlite3,hashlib,re,random,sys
from PyQt5.QtCore import Qt


con = sqlite3.connect('library.db')
cursor =  con.cursor()

cursor.execute("SELECT * FROM Books")
rows = cursor.fetchall()

data = []

for row in rows:
	data.append(list(row))

try:
	cursor.execute('CREATE TABLE Users (id integer PRIMARY KEY, Name text, Surname text, Email text, Password text)')
except sqlite3.OperationalError:
	pass

try:
	cursor.execute('CREATE TABLE Books (id integer PRIMARY KEY, Title text, Author text, Publisher text, Year text, ISBN text)')
except sqlite3.OperationalError:
	pass

try:
	cursor.execute('CREATE TABLE Albums (id integer PRIMARY KEY, AlbumId text, Title text, ArtistId text)')
except sqlite3.OperationalError:
	pass

con.commit()

class Login(object):
	def setupUi(self, MainWindow1):
		MainWindow1.setObjectName("MainWindow1")
		MainWindow1.resize(192, 110)
		self.centralwidget = QtWidgets.QWidget(MainWindow1)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(20, 20, 35, 10))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(20, 50, 35, 10))
		self.label_2.setObjectName("label_2")
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(60, 20, 113, 20))
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(60, 50, 113, 20))
		self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(30, 80, 56, 17))
		self.pushButton.setObjectName("pushButton")
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(110, 80, 56, 17))
		self.pushButton_2.setObjectName("pushButton_2")
		MainWindow1.setCentralWidget(self.centralwidget)

		self.pushButton.clicked.connect(self.login)
		self.pushButton_2.clicked.connect(self.register)

		self.retranslateUi(MainWindow1)
		QtCore.QMetaObject.connectSlotsByName(MainWindow1)

	def register(self):
		MainWindow.show()
		MainWindow1.hide()

	def login(self):
		log = self.lineEdit.text()
		password = self.lineEdit_2.text()
		passw = hashlib.sha256(password.encode()).hexdigest()
		check = cursor.execute('SELECT * FROM Users WHERE Email = ? AND Password = ?', (log,passw))
		login = check.fetchall()
		if log == 'a' and password=='a':
			MainWindow1.hide()
			Console.show()
		if login == [] and log != 'a' and password != 'a':
			msg = QMessageBox()
			msg.setWindowTitle('Log in failed')
			msg.setText('This account does not exist in the system')
			msg.exec_()
		else:
			MainWindow1.hide()
			Console.show()


	def retranslateUi(self, MainWindow1):
		_translate = QtCore.QCoreApplication.translate
		MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow1"))
		self.label.setText(_translate("MainWindow1", "Login:"))
		self.label_2.setText(_translate("MainWindow1", "Password:"))
		self.pushButton.setText(_translate("MainWindow1", "Log In"))
		self.pushButton_2.setText(_translate("MainWindow1", "Sign Up"))

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(233, 186)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(30, 10, 35, 10))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(30, 40, 35, 10))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(30, 70, 35, 10))
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(30, 100, 35, 10))
		self.label_4.setObjectName("label_4")
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(80, 10, 113, 20))
		self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(80, 40, 113, 20))
		self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_3.setGeometry(QtCore.QRect(80, 70, 113, 20))
		self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_4.setGeometry(QtCore.QRect(80, 100, 113, 20))
		self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(10, 130, 211, 51))
		self.pushButton.setObjectName("pushButton")

		self.pushButton.clicked.connect(self.write)

		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "Name:"))
		self.label_2.setText(_translate("MainWindow", "Surname:"))
		self.label_3.setText(_translate("MainWindow", "E-mail:"))
		self.label_4.setText(_translate("MainWindow", "Password:"))
		self.pushButton.setText(_translate("MainWindow", "Register"))


	def write(self):
	#	ui1.show()
		self.name = self.lineEdit.text()
		self.surname = self.lineEdit_2.text()
		self.mail = self.lineEdit_3.text()
		self.password = self.lineEdit_4.text()
		self.passw = hashlib.sha256(self.password.encode()).hexdigest()

		self.uppercase = False
		self.num = False
		self.chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

		check1 = cursor.execute('SELECT * FROM Users WHERE Email = ? AND Password = ?', (self.mail,self.passw))
		done = check1.fetchall()

		params = (self.name,self.surname,self.mail,self.passw)
		if self.name=='' or self.surname=='' or self.mail=='' or self.password=='':
			msg = QMessageBox()
			msg.setWindowTitle('Error')
			msg.setText('You have not filled all the fields!')
			msg.exec_()
			MainWindow.hide()
			MainWindow1.show()
		if done == [] and self.chars.search(self.password) != None:
			cursor.execute('INSERT INTO Users VALUES (NULL,?,?,?,?)',params)
			msg = QMessageBox()
			msg.setWindowTitle('Account Created')
			msg.setText('Congratulations! You have created a new account!')
			msg.exec_()
			MainWindow.hide()
			MainWindow1.show()
		if done != []:
			msg = QMessageBox()
			msg.setWindowTitle('Account Exists')
			msg.setText('Sorry, the account with these details already exsists.')
			msg.exec_()
			MainWindow.hide()
			MainWindow1.show()
		if '.' not in self.mail or '@' not in self.mail:
			msg = QMessageBox()
			msg.setWindowTitle('Error')
			msg.setText('The mail you have entered is wrong!')
			msg.exec_()
		if len(self.password)<8:
			msg = QMessageBox()
			msg.setWindowTitle('Error')
			msg.setText('Your password is too short. It should be at least 8 characters long.')
			msg.exec_()
		if self.chars.search(self.password) == None:
			msg = QMessageBox()
			msg.setWindowTitle('Error')
			msg.setText('Your password should contain at least one special character.')
			msg.exec_()
		for i in range(len(self.password)):
			if self.password[i].isupper():
				self.uppercase = True
			if self.password[i].isdigit():
				self.num = True
		if self.uppercase == False:
			msg = QMessageBox()
			msg.setWindowTitle('Error')
			msg.setText('Your password should contain at least one capital letter.')
			msg.exec_()
		if self.num == False:
			msg = QMessageBox()
			msg.setWindowTitle('Error')
			msg.setText('Your password should contain at least one number.')
			msg.exec_()
		con.commit()

con = sqlite3.connect('library.db')
cursor =  con.cursor()
cursor.execute("SELECT * FROM Books")
rows = cursor.fetchall()
data = []

for row in rows:
	data.append(list(row))

class Console(object):
	def setupUi(self, MainWindow):
		super().__init__()
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(779, 526)
		MainWindow.setTabletTracking(False)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.NewButton = QtWidgets.QPushButton(self.centralwidget)
		self.centralwidget2 = QtWidgets.QWidget(self.centralwidget)
		self.centralwidget2.setObjectName("centralwidget")
		self.tableView = QtWidgets.QTableView(self.centralwidget2)
		self.tableView.setGeometry(QtCore.QRect(20, 20, 661, 441))
		self.NewButton.setGeometry(QtCore.QRect(700, 60, 56, 17))
		self.NewButton.setObjectName("NewButton")
		self.searchButton = QtWidgets.QPushButton(self.centralwidget)
		self.searchButton.setGeometry(QtCore.QRect(700, 90, 56, 17))
		self.searchButton.setObjectName("searchButton")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 18))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)

		self.table = QtWidgets.QTableView()

		self.model = TableModel(data)
		self.table.setModel(self.model)

		MainWindow.setCentralWidget(self.table)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.NewButton.clicked.connect(self.new)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.NewButton.setText(_translate("MainWindow", "New"))
		self.searchButton.setText(_translate("MainWindow", "Search"))

	def new(self):
		newBook.show()


class Ui_NewBookDialog(object):
	def setupUi(self, NewBookDialog):
		NewBookDialog.setObjectName("NewBookDialog")
		NewBookDialog.resize(232, 181)
		self.buttonBox = QtWidgets.QDialogButtonBox(NewBookDialog)
		self.buttonBox.setGeometry(QtCore.QRect(80, 150, 121, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.label = QtWidgets.QLabel(NewBookDialog)
		self.label.setGeometry(QtCore.QRect(30, 10, 51, 16))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(NewBookDialog)
		self.label_2.setGeometry(QtCore.QRect(30, 40, 51, 16))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(NewBookDialog)
		self.label_3.setGeometry(QtCore.QRect(30, 70, 61, 16))
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(NewBookDialog)
		self.label_4.setGeometry(QtCore.QRect(30, 100, 41, 16))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(NewBookDialog)
		self.label_5.setGeometry(QtCore.QRect(30, 130, 41, 16))
		self.label_5.setObjectName("label_5")
		self.TitleInput = QtWidgets.QLineEdit(NewBookDialog)
		self.TitleInput.setGeometry(QtCore.QRect(90, 10, 113, 20))
		self.TitleInput.setObjectName("TitleInput")
		self.AuthorInput = QtWidgets.QLineEdit(NewBookDialog)
		self.AuthorInput.setGeometry(QtCore.QRect(90, 40, 113, 20))
		self.AuthorInput.setObjectName("AuthorInput")
		self.PublisherInput = QtWidgets.QLineEdit(NewBookDialog)
		self.PublisherInput.setGeometry(QtCore.QRect(90, 70, 113, 20))
		self.PublisherInput.setObjectName("PublisherInput")
		self.YearInput = QtWidgets.QLineEdit(NewBookDialog)
		self.YearInput.setGeometry(QtCore.QRect(90, 100, 113, 20))
		self.YearInput.setObjectName("YearInput")
		self.ISBNInput = QtWidgets.QLineEdit(NewBookDialog)
		self.ISBNInput.setGeometry(QtCore.QRect(90, 130, 113, 20))
		self.ISBNInput.setObjectName("ISBNInput")

		self.retranslateUi(NewBookDialog)
		self.buttonBox.clicked.connect(NewBookDialog.accept)
		self.buttonBox.rejected.connect(NewBookDialog.reject)
		self.buttonBox.accepted.connect(self.ok)
		QtCore.QMetaObject.connectSlotsByName(NewBookDialog)

	def ok(self):
		params = (self.TitleInput.text(),self.AuthorInput.text(), self.PublisherInput.text(),self.YearInput.text(),self.ISBNInput.text())
		cursor.execute('INSERT INTO Books VALUES (NULL,?,?,?,?,?)',params)
		codes = []
		i=0
		while len(codes) < 3503:
			num = random.randint(1000000000,1000000000000)
			if num in codes:
				pass
			else:
				codes.append(num)
		for row in rows:
			row = (str(row[1]),row[5],str(row[0]),'N/A',codes[i])
		#	print(row)
			cursor.execute('INSERT INTO Books VALUES (NULL,?,?,?,?,?)',row)
			i+=1
		con.commit()

	def retranslateUi(self, NewBookDialog):
		_translate = QtCore.QCoreApplication.translate
		NewBookDialog.setWindowTitle(_translate("NewBookDialog", "NewBookDialog"))
		self.label.setText(_translate("NewBookDialog", "Book Title"))
		self.label_2.setText(_translate("NewBookDialog", "Book Author"))
		self.label_3.setText(_translate("NewBookDialog", "Book Publisher"))
		self.label_4.setText(_translate("NewBookDialog", "Book Year"))
		self.label_5.setText(_translate("NewBookDialog", "Book ISBN"))


class TableModel(QtCore.QAbstractTableModel):
	def __init__(self,data):
		super(TableModel,self).__init__()
		self._data = data

	def data(self,index,role):
		if role == Qt.DisplayRole:
			return self._data[index.row()][index.column()]

	def rowCount(self,index):
		return len(self._data)

	def columnCount(self,index):
		return len(self._data[0])

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.table = QtWidgets.QTableView()
		self.model = TableModel(data)
		self.table.setModel(self.model)

		self.setCentralWidget(self.table)

class Ui_Console(object):
	def setupUi(self, Console):
		Console.setObjectName("Console")
		Console.resize(779, 526)
		Console.setTabletTracking(False)
		self.centralwidget = QtWidgets.QWidget(Console)
		self.centralwidget.setObjectName("centralwidget")
		self.NewButton = QtWidgets.QPushButton(self.centralwidget)
		self.NewButton.setGeometry(QtCore.QRect(700, 60, 56, 17))
		self.NewButton.setObjectName("NewButton")
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(700, 90, 56, 17))
		self.pushButton_2.setObjectName("pushButton_2")
		self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget.setGeometry(QtCore.QRect(20, 20, 611, 441))
		self.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setGeometry(QtCore.QRect(700, 120, 56, 17))
		self.pushButton_3.setObjectName("pushButton_3")
		self.tableWidget.setColumnCount(6)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setHorizontalHeaderLabels(['ID','Title','Author','Publisher','Year','ISBN'])
		Console.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(Console)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 22))
		self.menubar.setObjectName("menubar")
		Console.setMenuBar(self.menubar)

		self.tableWidget.setSortingEnabled(True)

		self.pushButton_2.clicked.connect(self.search)
		self.pushButton_3.clicked.connect(self.update)


		self.retranslateUi(Console)
		QtCore.QMetaObject.connectSlotsByName(Console)

		for i in data:
			self.addTableRow(self.tableWidget, i)

	def addTableRow(self, table, row_data):
		row = self.tableWidget.rowCount()
		self.tableWidget.setRowCount(row+1)
		col = 0
		for item in row_data:
			cell = QTableWidgetItem(str(item))
			self.tableWidget.setItem(row, col, cell)
			col += 1


	def retranslateUi(self, Console):
		_translate = QtCore.QCoreApplication.translate
		Console.setWindowTitle(_translate("Console", "MainWindow"))
		self.NewButton.setText(_translate("Console", "New"))
		self.pushButton_2.setText(_translate("Console", "Search"))
		self.pushButton_3.setText(_translate("Console", "Update Table"))

	def search(self,find):
		search_dialog.show()



	def update_table(self,data):
		self.tableWidget.clear()
		self.tableWidget.setRowCount(0)
		self.tableWidget.setHorizontalHeaderLabels(['ID','Title','Author','Publisher','Year','ISBN'])
		display_data=[]
		for entry in data:
			display_data.append(list(entry))
		for i in display_data:
			self.addTableRow(self.tableWidget, i)

	def update(self):
		self.tableWidget.clear()
		self.tableWidget.setRowCount(0)
		self.tableWidget.setHorizontalHeaderLabels(['ID','Title','Author','Publisher','Year','ISBN'])
		for i in data:
			self.addTableRow(self.tableWidget, i)

class Ui_search_dialog(object):
	def setupUi(self, search_dialog):
		search_dialog.setObjectName("search_dialog")
		search_dialog.resize(183, 120)
		self.centralwidget = QtWidgets.QWidget(search_dialog)
		self.centralwidget.setObjectName("centralwidget")
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(50, 20, 113, 20))
		self.lineEdit.setObjectName("lineEdit")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(10, 0, 121, 16))
		self.label.setObjectName("label")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(50, 50, 113, 20))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(10, 20, 35, 10))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(10, 50, 35, 10))
		self.label_3.setObjectName("label_3")
		self.ok_button = QtWidgets.QPushButton(self.centralwidget)
		self.ok_button.setGeometry(QtCore.QRect(10, 80, 71, 21))
		self.ok_button.setObjectName("ok_button")
		self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
		self.cancel_button.setGeometry(QtCore.QRect(85, 80, 81, 21))
		self.cancel_button.setObjectName("cancel_button")
		search_dialog.setCentralWidget(self.centralwidget)

		self.ok_button.clicked.connect(self.ok)

		self.retranslateUi(search_dialog)
		QtCore.QMetaObject.connectSlotsByName(search_dialog)

	def retranslateUi(self, search_dialog):
		_translate = QtCore.QCoreApplication.translate
		search_dialog.setWindowTitle(_translate("search_dialog", "Search"))
		self.label.setText(_translate("search_dialog", "What do you want to search for?"))
		self.label_2.setText(_translate("search_dialog", "Title:"))
		self.label_3.setText(_translate("search_dialog", "Author:"))
		self.ok_button.setText(_translate("search_dialog", "OK"))
		self.cancel_button.setText(_translate("search_dialog", "Cancel"))

	def ok(self):
		title = self.lineEdit.text()
		author = self.lineEdit_2.text()
		if title == '' and author == '':
			message = QMessageBox()
			message.setWindowTitle('Error')
			message.setText('You have not filled the fields!')
			message.exec_()
		else:
			params=[]
			params.append(author)
			params.append(title)
			check = cursor.execute('SELECT * FROM Books WHERE Author = ? OR Title = ?', params)
			find=check.fetchall()
			Ui_Console.update_table(ui,find)
		search_dialog.hide()


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	app2 = QtWidgets.QApplication(sys.argv)
	app3 = QtWidgets.QApplication(sys.argv)


	MainWindow = QtWidgets.QMainWindow()
	MainWindow1 = QtWidgets.QMainWindow()
	ConsoleWin = QtWidgets.QMainWindow()
	newBook = QtWidgets.QDialog()
	MainWindow2 = QtWidgets.QMainWindow()
	Console = QtWidgets.QMainWindow()
	search_dialog = QtWidgets.QMainWindow()

	uiMain = Ui_MainWindow()
	uiMain.setupUi(MainWindow)

	ui = Ui_Console()
	ui.setupUi(Console)
	ui2 = Ui_search_dialog()
	ui2.setupUi(search_dialog)
	Console.hide()

	ui1 = Login()
	ui1.setupUi(MainWindow1)



	newBookUi = Ui_NewBookDialog()
	newBookUi.setupUi(newBook)

	MainWindow1.show()
	newBook.hide()

	sys.exit(app.exec_())
	sys.exit(app3.exec_())
	sys.exit(app2.exec_())
