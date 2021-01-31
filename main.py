# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QWidget, QApplication, QPushButton, QVBoxLayout, QMessageBox
from aiogram import Bot
import asyncio
from time import sleep

loop = asyncio.get_event_loop()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(338, 326)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 31, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(230, 40, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 71, 21))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(240, 200, 61, 21))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(194, 160, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setEnabled(False)
        self.spinBox_2.setGeometry(QtCore.QRect(240, 230, 61, 21))
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(3600)
        self.spinBox_2.setProperty("value", 0)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 230, 51, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(230, 80, 91, 71))
        self.label_5.setLineWidth(1)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 160, 161, 61))
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 41, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 230, 51, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 260, 131, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 200, 41, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(310, 230, 31, 21))
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 338, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.closeEvent = self.closeEvent
        MainWindow.setMenuBar(self.menubar)
        self.label_2.setBuddy(self.lineEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "v 0.1"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.label_2.setText(_translate("MainWindow", "Bot Token:"))
        self.pushButton_2.setText(_translate("MainWindow", "Send message"))
        self.label_4.setText(_translate("MainWindow", "Sleepeng"))
        self.label_5.setText(_translate("MainWindow", "Authorized as:"))
        self.lineEdit_2.setText(_translate("MainWindow", "Hell World!"))
        self.label_6.setText(_translate("MainWindow", "Text:"))
        self.label_7.setText(_translate("MainWindow", "User ID:"))
        self.lineEdit_3.setText(_translate("MainWindow", "704477361"))
        self.label_8.setText(_translate("MainWindow", "times"))
        self.label_9.setText(_translate("MainWindow", "secs"))

    def enableBox2(self):
        if self.spinBox.value() > 1:
            self.spinBox_2.setEnabled(True)
        else:
            self.spinBox_2.setEnabled(False)

    def sending(self):
        global bot
        try:
            for i in range(self.spinBox.value()):
                QtWidgets.QApplication.processEvents()
                loop.run_until_complete(bot.send_message(
                    self.lineEdit_3.text(),
                    self.lineEdit_2.text()
                ))
                if self.spinBox.value() > 1:
                    sleep(self.spinBox_2.value())

        except Exception as err:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText(f"Error sending message to {self.lineEdit_3.text()} | {err}")
            msgBox.setWindowTitle("Sending error")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec()

    def loginbot(self):
        global bot
        try:
            QtWidgets.QApplication.processEvents()
            bot = Bot(
                token=self.lineEdit.text()
            )
            self.label_5.setText(f'Authorized as:\n@{(loop.run_until_complete(bot.get_me())).username}')
            self.pushButton_2.setEnabled(True)
        except Exception as err:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText(f"Connecting to bot error | {err}")
            msgBox.setWindowTitle("ERR")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec()

    def set_clicks(self):
        self.pushButton.clicked.connect(self.loginbot)
        self.spinBox.valueChanged.connect(self.enableBox2)
        self.pushButton_2.clicked.connect(self.sending)

    def closeEvent(self, event):
        global bot
        try:
            QtWidgets.QApplication.processEvents()
            loop.run_until_complete(bot.close())
        except Exception as err:
            print(err)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.set_clicks()
    MainWindow.show()
    sys.exit(app.exec_())
