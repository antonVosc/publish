from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QAbstractItemView
from past.builtins import xrange

items = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(256, 187)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Add_button = QtWidgets.QPushButton(self.centralwidget)
        self.Add_button.setGeometry(QtCore.QRect(190, 20, 56, 17))
        self.Add_button.setObjectName("Add_button")
        self.Edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.Edit_button.setGeometry(QtCore.QRect(190, 50, 56, 17))
        self.Edit_button.setObjectName("Edit_button")
        self.Remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.Remove_button.setGeometry(QtCore.QRect(190, 80, 56, 17))
        self.Remove_button.setObjectName("Remove_button")
        self.Sort_button = QtWidgets.QPushButton(self.centralwidget)
        self.Sort_button.setGeometry(QtCore.QRect(190, 110, 56, 17))
        self.Sort_button.setObjectName("Sort_button")
        self.SortBack_button = QtWidgets.QPushButton(self.centralwidget)
        self.SortBack_button.setGeometry(QtCore.QRect(190, 140, 56, 17))
        self.SortBack_button.setObjectName("SortBack_button")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 171, 161))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.Add_button.clicked.connect(self.add)
        self.Edit_button.clicked.connect(self.edit)
        self.Sort_button.clicked.connect(self.sort)
        self.SortBack_button.clicked.connect(self.sort_back)
        self.Remove_button.clicked.connect(self.remove)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Add_button.setText(_translate("MainWindow", "Add"))
        self.Edit_button.setText(_translate("MainWindow", "Edit"))
        self.Remove_button.setText(_translate("MainWindow", "Remove"))
        self.Sort_button.setText(_translate("MainWindow", "Sort A-Z"))
        self.SortBack_button.setText(_translate("MainWindow", "Sort Z-A"))

    def add(self):
        add_item, ok = QtWidgets.QInputDialog.getText(None,"Add", "What do you want to add to list?",QtWidgets.QLineEdit.Normal,"")
        self.listWidget.addItem(add_item)

    def edit(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        newVal, ok = QtWidgets.QInputDialog.getText(None,"Edit", "What is the new item?",QtWidgets.QLineEdit.Normal,item.text())
        item.setText(newVal)

    def sort(self):
        items=[]
        for i in xrange(self.listWidget.count()):
            items.append(self.listWidget.item(i).text())
        items.sort()
        self.listWidget.clear()
        for i in range(len(items)):
            self.listWidget.addItem(items[i])

    def sort_back(self):
        items=[]
        for i in xrange(self.listWidget.count()):
            items.append(self.listWidget.item(i).text())
        items.sort(reverse=True)
        self.listWidget.clear()
        for i in range(len(items)):
            self.listWidget.addItem(items[i])

    def remove(self):
        for item in self.listWidget.selectedItems():
            self.listWidget.takeItem(self.listWidget.row(item))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
