from PyQt5 import QtCore, QtGui, QtWidgets
import requests, json


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 341)
        self.api_key = "8f23a1347177d649fd3afc4d97f09bb1"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 30, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 30, 261, 41))
        self.textEdit.setObjectName("textEdit")
        self.font = QtGui.QFont("Times",25)
        self.textEdit.setFont(self.font)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(110, 110, 241, 131))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.get_weather)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Get Weather"))

    def lengths(self,line):
        self.line = line
        self.sp = ' '
        for i in range(40-(len(self.line)//2)):
            self.sp=self.sp + " "
        f_line = self.sp + self.line
        return f_line

    def get_weather(self):
        self.city_name = self.textEdit.toPlainText()
        self.complete_url = self.base_url + "appid=" + self.api_key + "&q=" + self.city_name
        self.response = requests.get(self.complete_url)
        self.x = self.response.json()
        self.cond=self.x['weather'][0]['main']
        self.detailes=self.x['weather'][0]['description']
        self.temp = self.x['main']['temp']
        self.kelvin = self.temp
        self.celcius = self.kelvin-273.15
        line_1 = self.lengths('City - '+self.city_name)
        line_2 = self.lengths('C: '+str(self.celcius))
        line_3 = self.lengths('Conditions: '+str(self.cond)+', Detailes: '+str(self.detailes))

        self.textBrowser.setText(line_1+"\n"+line_2+"\n"+line_3+"\n")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
