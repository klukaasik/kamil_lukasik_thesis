from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog, QWidget

import os
from os.path import splitext
from collections import Counter
import time
from rich import print
import shutil

import whisper
import stable_whisper

import player

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.filename = ""
        self.model_name = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(100, 20, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.chooseModelComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseModelComboBox.setGeometry(QtCore.QRect(200, 160, 511, 22))
        self.chooseModelComboBox.setToolTip("")
        self.chooseModelComboBox.setStatusTip("")
        self.chooseModelComboBox.setWhatsThis("")
        self.chooseModelComboBox.setAccessibleName("")
        self.chooseModelComboBox.setStyleSheet("")
        self.chooseModelComboBox.setEditable(False)
        self.chooseModelComboBox.setObjectName("chooseModelComboBox")
        self.chooseModelComboBox.addItem("")
        self.chooseModelComboBox.addItem("")
        self.chooseModelComboBox.addItem("")
        self.chooseModelComboBox.addItem("")
        self.chooseModelComboBox.addItem("")
        self.transcribeButton = QtWidgets.QPushButton(self.centralwidget)
        self.transcribeButton.setGeometry(QtCore.QRect(410, 210, 75, 23))
        self.transcribeButton.setObjectName("transcribeButton")
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(170, 300, 571, 311))
        self.tableView.setObjectName("tableView")
        self.tableView.setColumnCount(1)
        number = self.get_data()
        self.tableView.setRowCount(number)

        self.tableView.setColumnWidth(0, 553)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(0, item)
        self.tableView.horizontalHeader().setMinimumSectionSize(39)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 90, 511, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.browseFileEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.browseFileEdit.setReadOnly(True)
        self.browseFileEdit.setObjectName("browseFileEdit")
        self.horizontalLayout.addWidget(self.browseFileEdit)
        self.browseFileButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.browseFileButton.setObjectName("browseFileButton")
        self.horizontalLayout.addWidget(self.browseFileButton)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 650, 71, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 250, 401, 20))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.load_data()

        self.tableView.clicked.connect(self.get_row)
        self.browseFileButton.clicked.connect(self.browse_file)
        self.transcribeButton.clicked.connect(self.transcribe)
        self.pushButton.clicked.connect(self.goToPlayer)
        self.pushButton.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        self.chooseModelComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Platform Supporting Correction for Speech to Text Conversion "))
        self.title.setText(_translate("MainWindow", "Platform Supporting Correction for Speech to Text Conversion "))
        self.chooseModelComboBox.setPlaceholderText(_translate("MainWindow", "Wybierz model..."))
        self.chooseModelComboBox.setItemText(0, _translate("MainWindow", "Tiny"))
        self.chooseModelComboBox.setItemText(1, _translate("MainWindow", "Base"))
        self.chooseModelComboBox.setItemText(2, _translate("MainWindow", "Small"))
        self.chooseModelComboBox.setItemText(3, _translate("MainWindow", "Medium"))
        self.chooseModelComboBox.setItemText(4, _translate("MainWindow", "Large"))
        self.transcribeButton.setText(_translate("MainWindow", "Transkrybuj"))
        item = self.tableView.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nazwa pliku"))
        self.browseFileButton.setText(_translate("MainWindow", "Przeglądaj pliki..."))
        self.pushButton.setText(_translate("MainWindow", "Odtwórz"))

    def goToPlayer(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = player.Ui_Form(self.filename)
        self.ui.setupUi(self.window)
        self.window.show()

    def clear(self):
        self.label.setText("")

    def transcribe(self):
        try:
            if self.filename[0].endswith(".mp3"):
                self.label.setText("")
                self.filename = self.filename[0]
                self.model_name = self.getModel().lower()

                self.transcriber(self.filename, self.model_name)
                self.label.setStyleSheet('color: green')
                self.label.setText("Transkypcja udana!")
                self.browseFileEdit.clear()
                self.filename = ""
                QTimer.singleShot(3000, self.clear)

            else:
                self.label.setStyleSheet('color: red')
                self.label.setText("Niepoprawne rozszerzenie pliku! (tylko mp3)")
        except:
            self.label.setStyleSheet('color: red')
            self.label.setText("Nie wprowadzono pliku!")

    def get_data(self):
        i = 0
        myDir = os.listdir("transcriptions/")
        l = [splitext(filename)[0] for filename in myDir]
        a = dict(Counter(l))

        for k, v in a.items():
            if v > 1:
                i += 1

        return i

    def load_data(self):
        list = []

        myDir = os.listdir("transcriptions/")
        l = [splitext(filename)[0] for filename in myDir]
        a = dict(Counter(l))

        for k, v in a.items():
            if v > 1:
                print(k)
                list.append(k)
        row = 0

        for el in list:
            self.tableView.setItem(row, 0, QtWidgets.QTableWidgetItem(el + ".mp3"))
            row = row + 1
            print(row)
            print(el)

    def get_row(self):
        try:
            self.pushButton.setEnabled(True)
            row = self.tableView.currentRow()
            item = self.tableView.item(row, 0).text()
            self.filename = item
        except:
            self.pushButton.setEnabled(False)

    def browse_file(self):
        self.filename = QFileDialog.getOpenFileName()
        self.browseFileEdit.unsetCursor()
        self.browseFileEdit.setText(self.filename[0])
        try:
            if self.filename[0].endswith(".mp3"):
                print(os.getcwd(), 'transcriptions', self.filename[0])
                shutil.copy(self.filename[0], os.path.join(os.getcwd(), 'transcriptions'))
        except:
            print("file already exists")

    def getModel(self):
        self.model = self.chooseModelComboBox.currentText()
        return self.model

    def transcriber(self, file_name, model_name):
        start = time.time()

        model = whisper.load_model(model_name)
        stable_whisper.modify_model(model)
        result = model.transcribe(file_name, fp16=False)

        file_name = file_name.split('.', 1)[0]
        file_name = file_name.rsplit('/', 1)[1]
        print(file_name)
        stable_whisper.results_to_word_srt(result, 'transcriptions/' + file_name + '.srt', combine_compound=True, strip=True)

        end = time.time()
        hours, rem = divmod(end - start, 3600)
        minutes, seconds = divmod(rem, 60)

        number = self.get_data()
        self.tableView.setRowCount(number)
        self.load_data()

        duration = "{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds)
        print(duration)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
