from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QColor, QSyntaxHighlighter, QTextCharFormat, QTextFormat
from PyQt5.Qt import Qt

import os
import pysrt
from PyQt5.QtWidgets import QPlainTextEdit, QTextEdit

import app


class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super().__init__(parent)
        self._highlight_lines = {}

    def highlight_line(self, line_num, fmt):
        if isinstance(line_num, int) and line_num >= 0 and isinstance(fmt, QTextCharFormat):
            self._highlight_lines[line_num] = fmt
            block = self.document().findBlockByLineNumber(line_num)
            self.rehighlightBlock(block)

    # def clear_highlight(self):
    #     self._highlight_lines = {}
    #     self.rehighlight()

    def highlightBlock(self, text):
        blockNumber = self.currentBlock().blockNumber()
        fmt = self._highlight_lines.get(blockNumber)
        if fmt is not None:
            self.setFormat(0, len(text), fmt)


class Ui_Form(object):
    def __init__(self, filename):
        self.filename = filename
        super().__init__()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(867, 646)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        Form.setFont(font)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(13, 10, 841, 471))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(13, 10, 841, 471))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.playButton = QtWidgets.QPushButton(Form)
        self.playButton.setGeometry(QtCore.QRect(390, 550, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(8)
        self.playButton.setFont(font)
        self.playButton.setObjectName("playButton")
        self.volumeUpButton = QtWidgets.QPushButton(Form)
        self.volumeUpButton.setGeometry(QtCore.QRect(290, 580, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        self.volumeUpButton.setFont(font)
        self.volumeUpButton.setObjectName("volumeUpButton")
        self.volumeDownButton = QtWidgets.QPushButton(Form)
        self.volumeDownButton.setGeometry(QtCore.QRect(490, 580, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        self.volumeDownButton.setFont(font)
        self.volumeDownButton.setObjectName("volumeDownButton")
        self.pauseButton = QtWidgets.QPushButton(Form)
        self.pauseButton.setGeometry(QtCore.QRect(390, 610, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        self.pauseButton.setFont(font)
        self.pauseButton.setObjectName("pauseButton")
        self.slider = QtWidgets.QSlider(Form)
        self.slider.setGeometry(QtCore.QRect(90, 530, 761, 22))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setGeometry(QtCore.QRect(30, 490, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("pushButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 531, 73, 20))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        self.startLabel.setFont(font)
        self.startLabel.setObjectName("startLabel")
        self.horizontalLayout.addWidget(self.startLabel)
        self.slashLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        self.slashLabel.setFont(font)
        self.slashLabel.setObjectName("slashLabel")
        self.horizontalLayout.addWidget(self.slashLabel)
        self.endLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        self.endLabel.setFont(font)
        self.endLabel.setObjectName("endLabel")
        self.horizontalLayout.addWidget(self.endLabel)
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(744, 620, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.lineViewButton = QtWidgets.QPushButton(Form)
        self.lineViewButton.setGeometry(QtCore.QRect(624, 490, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        self.lineViewButton.setFont(font)
        self.lineViewButton.setObjectName("lineViewButton")
        self.wrappedViewButton = QtWidgets.QPushButton(Form)
        self.wrappedViewButton.setGeometry(QtCore.QRect(754, 490, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        self.wrappedViewButton.setFont(font)
        self.wrappedViewButton.setObjectName("wrappedViewButton")

        self.plusButton = QtWidgets.QPushButton(Form)
        self.plusButton.setGeometry(QtCore.QRect(640, 550, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.minusButton = QtWidgets.QPushButton(Form)
        self.minusButton.setGeometry(QtCore.QRect(754, 550, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.timer = QTimer()
        self.timer2 = QTimer()
        self.timer.timeout.connect(self.on_timeout_wrappedView)
        self.timer2.timeout.connect(self.on_timeout_lineView)
        self.start_time = 0
        self.start_time2 = 0
        self.end_time = 0
        self.i = 0
        self.i2 = 0
        self.alphaF = 1

        self.seconds = 0
        self.audio_duration = 0

        self.text_len = 0

        self.player = QMediaPlayer()

        self.loadFile(self.filename)

        self.loadText_lineView()
        self.loadText_wrapped()

        self.playButton.clicked.connect(self.playAudioFile)
        self.pauseButton.clicked.connect(self.pause_player)
        self.volumeUpButton.clicked.connect(self.volumeUp)
        self.volumeDownButton.clicked.connect(self.volumeDown)

        self.slider.sliderMoved.connect(self.set_position)
        self.slider.setDisabled(True)

        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)

        self.saveButton.clicked.connect(self.save)

        self.backButton.clicked.connect(self.back_to_menu)
        self.backButton.clicked.connect(Form.close)

        self.plainTextEdit.hide()

        self.lineViewButton.setEnabled(False)
        self.wrappedViewButton.setEnabled(True)

        self.lineViewButton.clicked.connect(self.clickLineViewButton)
        self.wrappedViewButton.clicked.connect(self.clickWrappedViewButton)

        self.plusButton.clicked.connect(self.transparencyUp)
        self.minusButton.clicked.connect(self.transparencyDown)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.playButton.setText(_translate("Form", "Play"))
        self.volumeUpButton.setText(_translate("Form", "Volume+"))
        self.volumeDownButton.setText(_translate("Form", "Volume-"))
        self.pauseButton.setText(_translate("Form", "Pause"))
        self.saveButton.setText(_translate("Form", "Zapisz"))
        self.startLabel.setText(_translate("Form", "00:00"))
        self.slashLabel.setText(_translate("Form", "/"))
        self.endLabel.setText(_translate("Form", "03:00"))
        self.backButton.setText(_translate("Form", "Powrót do menu"))
        self.lineViewButton.setText(_translate("Form", "Widok liniowy"))
        self.wrappedViewButton.setText(_translate("Form", "Sklejony tekst"))
        self.plusButton.setText(_translate("Form", "Przezroczystość +"))
        self.minusButton.setText(_translate("Form", "Przezroczystość -"))

    def clickLineViewButton(self):
        self.lineViewButton.setEnabled(False)
        self.wrappedViewButton.setEnabled(True)
        self.saveButton.setEnabled(True)
        self.plainTextEdit_2.show()
        self.plainTextEdit.hide()


    def clickWrappedViewButton(self):
        self.lineViewButton.setEnabled(True)
        self.wrappedViewButton.setEnabled(False)
        self.saveButton.setEnabled(False)
        self.plainTextEdit_2.hide()
        self.plainTextEdit.show()

    def transparencyUp(self):
        if self.alphaF < 1:
            self.alphaF += 0.05
            print("transparency: ", self.alphaF)
        else:
            self.alphaF = self.alphaF
            print("transparency: ", self.alphaF)

    def transparencyDown(self):
        if self.alphaF > 0:
            self.alphaF -= 0.05
            print("transparency: ", self.alphaF)
        else:
            self.alphaF = self.alphaF
            print("transparency: ", self.alphaF)

    def volumeUp(self):
        currentVolume = self.player.volume()
        self.player.setVolume(currentVolume + 5)
        print(currentVolume)

    def volumeDown(self):
        currentVolume = self.player.volume()
        self.player.setVolume(currentVolume - 5)
        print(currentVolume)

    def pause_player(self):
        self.seconds -= 1
        self.player.pause()
        self.timer.stop()
        self.timer2.stop()
        self.playButton.setEnabled(True)

    def loadFile(self, filename):
        full_file_path = os.path.join(os.getcwd(), 'transcriptions/', filename)
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)

    def playAudioFile(self):
        self.seconds -= 1
        print(self.start_time)
        if self.start_time == 0 and self.start_time2 == 0:
            self.timer = QTimer()
            self.timer2 = QTimer()
            self.timer.timeout.connect(self.on_timeout_wrappedView)
            self.timer2.timeout.connect(self.on_timeout_lineView)
            self.start_time = 0
            self.start_time2 = 0
            self.end_time = 0
            self.i = 0
            self.i2 = 0

            self.seconds = 0

            self.player = QMediaPlayer()

            self.loadFile(self.filename)

            self.player.positionChanged.connect(self.position_changed)
            self.player.durationChanged.connect(self.duration_changed)

        self.player.play()
        self.playButton.setEnabled(False)
        duration = self.player.duration()

        try:
            self.end_time = duration
            print("endtime: ", self.end_time)
        except ValueError as e:
            print("error")
        else:
            self.timer.start()
            self.timer2.start()

    def loadText_lineView(self):
        subs = pysrt.open("transcriptions/" + self.filename.split('.', 1)[0] + ".srt")

        for sub in subs:
            self.plainTextEdit_2.appendPlainText(sub.text)
            print(str(sub.start.hours) + ":" + str(sub.start.minutes) + ":" + str(sub.start.seconds) + ":" + str(
                sub.start.milliseconds)
                  + " --- " + str(sub.end.hours) + ":" + str(sub.end.minutes) + ":" + str(sub.end.seconds) + ":" + str(
                sub.end.milliseconds))
            print(sub.end)
            milliseconds_start = sub.start.milliseconds + sub.start.seconds * 1000 + sub.start.minutes * 60000 + sub.start.hours * 60000 * 60
            milliseconds_end = sub.end.milliseconds + sub.end.seconds * 1000 + sub.end.minutes * 60000 + sub.end.hours * 60000 * 60
            duration = milliseconds_end - milliseconds_start
            print(duration)

    def loadText_wrapped(self):
        subs = pysrt.open("transcriptions/" + self.filename.split('.', 1)[0] + ".srt")

        for sub in subs:
            self.plainTextEdit.insertPlainText(sub.text + " ")
            print(str(sub.start.hours) + ":" + str(sub.start.minutes) + ":" + str(sub.start.seconds) + ":" + str(
                sub.start.milliseconds)
                  + " --- " + str(sub.end.hours) + ":" + str(sub.end.minutes) + ":" + str(sub.end.seconds) + ":" + str(
                sub.end.milliseconds))
            print(sub.end)
            milliseconds_start = sub.start.milliseconds + sub.start.seconds * 1000 + sub.start.minutes * 60000 + sub.start.hours * 60000 * 60
            milliseconds_end = sub.end.milliseconds + sub.end.seconds * 1000 + sub.end.minutes * 60000 + sub.end.hours * 60000 * 60
            duration = milliseconds_end - milliseconds_start
            print(duration)

    def position_changed(self, position):
        self.seconds += 1
        print("position: ", position)

        minutes, seconds = divmod(self.seconds, 60)
        time = "{:0>2}:{:05.2f}".format(int(minutes), seconds)
        self.startLabel.setText(time)

        print("timer: ", self.timer.remainingTime())
        print("timer2: ", self.timer2.remainingTime())
        self.slider.setValue(position)

    def duration_changed(self, duration):
        print("duration: ", duration)

        minutes, seconds = divmod(self.audio_duration, 60)
        time = "{:0>2}:{:05.2f}".format(int(minutes), seconds)
        self.endLabel.setText(time)

        # minutes, seconds = divmod(duration / 1000, 60)
        # time = "{:0>2}:{:05.2f}".format(int(minutes), seconds)
        # self.endLabel.setText(time)

        self.slider.setRange(0, self.audio_duration * 1000)

    def set_position(self, position):
        self.player.setPosition(position)

    def handle_errors(self):
        self.playButton.setEnabled(False)

    def onTextChanged(self, text):
        fmt = QTextCharFormat()
        fmt.setBackground(QColor('yellow'))
        # self.highlighter.clear_highlight()
        # self.highlighter2.clear_highlight()

        try:
            lineNumber = int(text) - 1
            self.highlighter.highlight_line(lineNumber, fmt)
        except ValueError:
            pass

    def on_timeout_lineView(self):
        subs = pysrt.open("transcriptions/" + self.filename.split('.', 1)[0] + ".srt")

        self.audio_duration = (subs[-1].end.milliseconds + subs[-1].end.seconds * 1000 + subs[
            -1].end.minutes * 60000 + subs[-1].end.hours * 60000 * 60) / 1000

        print("audio duration: ", self.audio_duration)

        if self.start_time2 <= self.audio_duration - 0.2:

            print(str(subs[self.i2].start.hours) + ":" + str(subs[self.i2].start.minutes) + ":" + str(
                subs[self.i2].start.seconds) + ":" + str(
                subs[self.i2].start.milliseconds)
                  + " --- " + str(subs[self.i2].end.hours) + ":" + str(subs[self.i2].end.minutes) + ":" + str(
                subs[self.i2].end.seconds) + ":" + str(
                subs[self.i2].end.milliseconds))
            print(subs[self.i2].end)
            milliseconds_start = subs[self.i2].start.milliseconds + subs[self.i2].start.seconds * 1000 + subs[
                self.i2].start.minutes * 60000 + subs[self.i2].start.hours * 60000 * 60
            milliseconds_end = subs[self.i2].end.milliseconds + subs[self.i2].end.seconds * 1000 + subs[
                self.i2].end.minutes * 60000 + subs[self.i2].end.hours * 60000 * 60
            duration = milliseconds_end - milliseconds_start

            if (self.i2 == 0 and subs[self.i2].start != "00:00:00,000"):
                end = subs[self.i2].end.milliseconds + subs[self.i2].end.seconds * 1000 + subs[
                    self.i2].end.minutes * 60000 + subs[self.i2].end.hours * 60000 * 60
                print("interval", end)
                self.timer2.setInterval(end)
                self.start_time2 += end / 1000

            elif len(subs) > self.i2 + 1 and subs[self.i2].end != subs[self.i2 + 1].start:
                end = subs[self.i2].end.milliseconds + subs[self.i2].end.seconds * 1000 + subs[
                    self.i2].end.minutes * 60000 + subs[self.i2].end.hours * 60000 * 60
                start = subs[self.i2 + 1].start.milliseconds + subs[self.i2 + 1].start.seconds * 1000 + subs[
                    self.i2 + 1].start.minutes * 60000 + subs[self.i2 + 1].start.hours * 60000 * 60
                duration = duration + start - end
                print("interval", duration)
                self.timer2.setInterval(duration)
                self.start_time2 += duration / 1000
            else:
                print("interval", duration)
                self.timer2.setInterval(duration)
                self.start_time2 += duration / 1000

            print("spent_time: ", self.start_time2)

            self.highlighter2 = SyntaxHighlighter(self.plainTextEdit_2.document())
            fmt = QTextCharFormat()
            color = QColor('yellow')
            color.setAlphaF(self.alphaF)
            fmt.setBackground(color)

            self.highlighter2.highlight_line(self.i2, fmt)

            self.i2 += 1

        else:
            self.seconds = -1
            self.timer2.disconnect()
            self.timer.disconnect()
            self.start_time = 0
            self.start_time2 = 0
            self.player.stop()
            self.playButton.setEnabled(True)

    def on_timeout_wrappedView(self):
        subs = pysrt.open("transcriptions/" + self.filename.split('.', 1)[0] + ".srt")

        self.audio_duration = (subs[-1].end.milliseconds + subs[-1].end.seconds * 1000 + subs[
            -1].end.minutes * 60000 + subs[-1].end.hours * 60000 * 60) / 1000

        print("audio duration: ", self.audio_duration)

        if self.start_time <= self.audio_duration - 0.2:

            print(str(subs[self.i].start.hours) + ":" + str(subs[self.i].start.minutes) + ":" + str(
                subs[self.i].start.seconds) + ":" + str(
                subs[self.i].start.milliseconds)
                  + " --- " + str(subs[self.i].end.hours) + ":" + str(subs[self.i].end.minutes) + ":" + str(
                subs[self.i].end.seconds) + ":" + str(
                subs[self.i].end.milliseconds))
            print(subs[self.i].end)
            milliseconds_start = subs[self.i].start.milliseconds + subs[self.i].start.seconds * 1000 + subs[
                self.i].start.minutes * 60000 + subs[self.i].start.hours * 60000 * 60
            milliseconds_end = subs[self.i].end.milliseconds + subs[self.i].end.seconds * 1000 + subs[
                self.i].end.minutes * 60000 + subs[self.i].end.hours * 60000 * 60
            duration = milliseconds_end - milliseconds_start

            if (self.i == 0 and subs[self.i].start != "00:00:00,000"):
                end = subs[self.i].end.milliseconds + subs[self.i].end.seconds * 1000 + subs[
                    self.i].end.minutes * 60000 + subs[self.i].end.hours * 60000 * 60
                print("interval", end)
                self.timer.setInterval(end)
                self.start_time += end / 1000

            elif len(subs) > self.i + 1 and subs[self.i].end != subs[self.i + 1].start:
                end = subs[self.i].end.milliseconds + subs[self.i].end.seconds * 1000 + subs[
                    self.i].end.minutes * 60000 + subs[self.i].end.hours * 60000 * 60
                start = subs[self.i + 1].start.milliseconds + subs[self.i + 1].start.seconds * 1000 + subs[
                    self.i + 1].start.minutes * 60000 + subs[self.i + 1].start.hours * 60000 * 60
                duration = duration + start - end
                print("interval", duration)
                self.timer.setInterval(duration)
                self.start_time += duration / 1000
            else:
                print("interval", duration)
                self.timer.setInterval(duration)
                self.start_time += duration / 1000

            print("spent_time: ", self.start_time)

            self.highlighter = SyntaxHighlighter(self.plainTextEdit.document())
            fmt = QTextCharFormat()
            fmt.setBackground(QColor('yellow'))
            color = QColor('yellow')
            color.setAlphaF(self.alphaF)
            fmt.setBackground(color)

            extraSelections = []

            selection = QTextEdit.ExtraSelection()
            selection.cursor = self.plainTextEdit.textCursor()
            selection.cursor.setPosition(self.text_len)
            self.text_len += len(subs[self.i].text) + 1
            selection.cursor.setPosition(self.text_len, QtGui.QTextCursor.KeepAnchor)
            selection.cursor.setCharFormat(fmt)

            selection.cursor.clearSelection()
            extraSelections.append(selection)
            self.plainTextEdit.setExtraSelections(extraSelections)

            self.i += 1

        else:
            self.seconds = -1
            self.timer.disconnect()
            self.timer2.disconnect()
            self.start_time = 0
            self.start_time2 = 0
            self.player.stop()
            self.playButton.setEnabled(True)

    def save(self):
        subs = pysrt.open("transcriptions/" + self.filename.split('.', 1)[0] + ".srt")

        modified_subs = self.plainTextEdit_2.toPlainText()

        f = open("transcriptions/subtitles.txt", "w")
        f.write(modified_subs)
        f.close()

        f = open("transcriptions/subtitles.txt", "r")

        i = 0

        for line in f:
            subs[i].text = line
            i += 1

        f.close()

        subs.save("transcriptions/" + self.filename.split('.', 1)[0] + ".srt")


    # def save(self):
    #     subs = pysrt.open("transcriptions/" + self.filename.split('.', 1)[0] + ".srt")
    #
    #     modified_subs = self.plainTextEdit.toPlainText()
    #
    #     f = open("transcriptions/subtitles_srt.txt", "w")
    #     f.write(subs.text)
    #     f.close()
    #
    #     f = open("transcriptions/subtitles_srt_old.txt", "w")
    #     f.write(subs.text)
    #     f.close()
    #
    #     f = open("transcriptions/subtitles.txt", "w")
    #     f.write(modified_subs)
    #     f.close()
    #
    #     f = open("transcriptions/subtitles_srt.txt", "r")
    #     f2 = open("transcriptions/subtitles.txt", "r")
    #
    #     i = 0
    #
    #     for ind, line in enumerate(f):
    #         line = line.replace("\n", "")
    #         sub_len = len(line) + 1
    #         line2 = f2.read(sub_len)
    #         line2 = line2.rstrip()
    #         if line != line2:
    #             print(ind, " xd: ", line2)
    #             subs[ind].text = line2.lstrip()
    #
    #     f.close()
    #
    #     subs.save("transcriptions/" + self.filename.split('.', 1)[0] + ".srt")

    def back_to_menu(self):
        self.player.stop()
        try:
            self.timer.disconnect()
            self.timer2.disconnect()
        except:
            print("error")
        self.window = QtWidgets.QMainWindow()
        self.ui = app.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
