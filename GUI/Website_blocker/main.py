from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(462, 399)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 61, 16))
        self.label_2.setObjectName("label_2")
        self.QLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.QLineEdit.setGeometry(QtCore.QRect(100, 100, 331, 21))
        self.QLineEdit.setObjectName("QLineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 35, 10))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 130, 331, 17))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(100, 180, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 180, 61, 191))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.website_list = self.blocked_websites()
        self.pushButton.clicked.connect(self.block_website)
        self.pushButton_2.clicked.connect(self.unblock_website)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Website Blocker"))
        self.label_2.setText(_translate("MainWindow", "Enter Website:"))
        self.label_3.setText(_translate("MainWindow", "Blocked:"))
        self.pushButton.setText(_translate("MainWindow", "Block"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("MainWindow", "Unblock"))


    def block_website(self):
        exist = False
        website = self.QLineEdit.text()
        with open('C:\Windows\System32\drivers\etc\hosts','r') as hosts:
            for i in hosts.readlines():
                if website in i:
                    exist = True
                    mes = QMessageBox()
                    mes.setText('The website is already blocked!')
                    mes.exec()
        if exist == False:
            if 'www.' in website:
                with open('C:\Windows\System32\drivers\etc\hosts','a') as hosts:
                    hosts.write('127.0.0.1\t'+website+'\n')
                    short_website = website.replace('www.','')
                    hosts.write('127.0.0.1\t'+short_website+'\n')
            else:
                full_website = 'www.'+website
                with open('C:\Windows\System32\drivers\etc\hosts','a') as hosts:
                    hosts.write('127.0.0.1\t'+website+'\n')
                    hosts.write('127.0.0.1\t'+full_website+'\n')
        self.blocked_websites()


    def blocked_websites(self):
        with open('C:\Windows\System32\drivers\etc\hosts','r') as hosts:
            host = hosts.readlines()
            websites = []
            counter = 0
            for i in host:
                write = False
                site_name = ''
                if 'www' not in i:
                    pass
                else:
                    for g in i:
                        if g == 'w':
                            write = True
                        if g == "\n":
                            write = False
                        if write == True:
                            site_name += g
                    websites.append(site_name)
                    elem = QtWidgets.QListWidgetItem()
                    self.listWidget.addItem(elem)
                    elem = self.listWidget.item(counter)
                    elem.setText(site_name)
                    counter += 1


    def unblock_website(self):
        global line_number
        items = self.listWidget.selectedItems()
        x=[]
        for i in list(items):
            x.append(str(i.text()))
        website_to_unblock = x[0]
        lines = open('C:\Windows\System32\drivers\etc\hosts').read().splitlines()
        for i in lines:
            if website_to_unblock in i:
                line_number = lines.index(i)
        list_of_lines = open('C:\Windows\System32\drivers\etc\hosts','r').readlines()
        list_of_lines[line_number-1] = ''
        list_of_lines[line_number] = ''
        write = open('C:\Windows\System32\drivers\etc\hosts','w')
        write.writelines(list_of_lines)
        write.close()
        mes = QMessageBox()
        mes.setText('You have unblocked the website!')
        mes.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
