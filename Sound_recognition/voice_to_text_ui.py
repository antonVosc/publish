import speech_recognition
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sounddevice as sd
import speech_recognition as sr
from scipy.io import wavfile


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 304)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 131, 32))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 60, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 70, 371, 201))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 60, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.read)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice recognition"))
        self.pushButton.setText(_translate("MainWindow", "Start recording"))
        self.label.setText(_translate("MainWindow", "Seconds:"))
        self.label_2.setText(_translate("MainWindow", "Output:"))

    def read(self):
        recogniser = sr.Recognizer()
        fr = 44100
        seconds = int(self.lineEdit.text())
        print('The recording has started')

        data = sd.rec(int(seconds*fr),samplerate=fr,channels=2)


        sd.wait()
        y = (np.iinfo(np.int32).max * (data/np.abs(data).max())).astype(np.int32)
        print('Finished recording')
        wavfile.write('new_rec.wav', fr, y)


        sound = sr.AudioFile('new_rec.wav')

        with sound as source:
            audio = recogniser.record(source)

        try:
            text = recogniser.recognize_google(audio)
            self.textEdit.setText(text)
        except speech_recognition.UnknownValueError:
            self.textEdit.setText("NO SOUND WAS DETECTED!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
