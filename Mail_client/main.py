from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import smtplib, socket

class Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(313, 150)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 60, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 100, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_2.clicked.connect(ui.login)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Log In"))
        self.pushButton.setText(_translate("MainWindow", "?"))
        self.label.setText(_translate("MainWindow", "Login:"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.pushButton_2.setText(_translate("MainWindow", "Log In"))

    def login(self):
        try:
            global s
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login(self.lineEdit.text(),self.lineEdit_2.text())
            self.message()
        except smtplib.SMTPAuthenticationError:
            error = QMessageBox()
            error.setWindowTitle('Error')
            error.setText('Log in failed! Check your details or try again later.')
            error.exec_()
        except TypeError:
            error = QMessageBox()
            error.setWindowTitle('Error')
            error.setText('Log in failed! Check your details or try again later.')
            error.exec_()
        except socket.gaierror:
            error = QMessageBox()
            error.setWindowTitle('Error')
            error.setText('Log in failed! Please check the internet connection and try again later.')
            error.exec_()

    def message(self):
        MainWindow.hide()
        MainWindow1.show()


class Message(object):
    def setupui1(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(812, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 60, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 560, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.To = QtWidgets.QLineEdit(self.centralwidget)
        self.To.setGeometry(QtCore.QRect(40, 10, 761, 31))
        self.To.setObjectName("To")
        self.Topic = QtWidgets.QLineEdit(self.centralwidget)
        self.Topic.setGeometry(QtCore.QRect(60, 50, 741, 31))
        self.Topic.setObjectName("Topic")
        self.Message = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Message.setGeometry(QtCore.QRect(10, 120, 791, 431))
        self.Message.setPlainText("")
        self.Message.setObjectName("Message")
        MainWindow1.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.message)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "Message"))
        self.label.setText(_translate("MainWindow1", "To:"))
        self.label_2.setText(_translate("MainWindow1", "Topic:"))
        self.label_3.setText(_translate("MainWindow1", "Message:"))
        self.pushButton.setText(_translate("MainWindow1", "Send"))

    def message(self):
        self.to_address = self.To.text()
        self.topic = self.Topic.text()
        self.mes = self.Message.document().toPlainText()
        self.send_message()

    def send_message(self):
        try:
            self.message = 'Subject: {}\n\n{}'.format(self.topic,self.mes)
            if ',' in self.to_address:
                self.to_address = self.to_address.split(',')
            self.send = s.sendmail(ui.lineEdit.text(),self.to_address,self.message)
            sent = QMessageBox()
            sent.setWindowTitle('Message sent')
            sent.setText('The message has successfully been sent!')
            sent.exec_()
            self.To.setText('')
            self.Topic.setText('')
            self.Message.clear()
        except smtplib.SMTPRecipientsRefused:
            error = QMessageBox()
            error.setWindowTitle('Error')
            error.setText('Some fields were not filled. Please go back and fill every field.')
            error.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app1 = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    MainWindow1 = QtWidgets.QMainWindow()

    ui = Login()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui1 = Message()
    ui1.setupui1(MainWindow1)
    MainWindow1.hide()

    sys.exit(app.exec_())
    sys.exit(app1.exec_())
