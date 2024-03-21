# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpwind.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton


class Ui_Help_window(object):
   
   

    def setupUi(self, Help_window):
        Help_window.setObjectName("Help_window")
        Help_window.resize(774, 533)
        Help_window.setStyleSheet("background-color: rgb(3,222,177);")
        self.label = QtWidgets.QLabel(Help_window)
        self.label.setGeometry(QtCore.QRect(10, 10, 331, 61))
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Help_window)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 171, 31))
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        
        self.textEdit = QtWidgets.QTextEdit(Help_window)
        self.textEdit.setGeometry(QtCore.QRect(190, 80, 261, 31))
        self.textEdit.setObjectName("textEdit")
        
        self.pushButton = QtWidgets.QPushButton(Help_window)
        self.pushButton.setGeometry(QtCore.QRect(10, 130, 101, 31))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(Help_window)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 490, 101, 31))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(Help_window)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 490, 101, 31))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtWidgets.QPushButton(Help_window)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 490, 101, 31))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.tableView = QtWidgets.QTableView(Help_window)
        self.tableView.setGeometry(QtCore.QRect(10, 180, 511, 291))
        self.tableView.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.tableView.setObjectName("tableView")
        self.textEdit_2 = QtWidgets.QTextEdit(Help_window)
        self.textEdit_2.setGeometry(QtCore.QRect(540, 90, 221, 371))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(Help_window)
        self.label_3.setGeometry(QtCore.QRect(600, 50, 121, 31))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(Help_window)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 80, 71, 31))
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.on_button_click)
        self.retranslateUi(Help_window)
        QtCore.QMetaObject.connectSlotsByName(Help_window)

    def retranslateUi(self, Help_window):
        _translate = QtCore.QCoreApplication.translate
        Help_window.setWindowTitle(_translate("Help_window", "Dialog"))
        self.label.setText(_translate("Help_window", "Импорт данных скважин"))
        self.label_2.setText(_translate("Help_window", "Путь к файлам"))
        self.pushButton.setText(_translate("Help_window", "Обновить"))
        self.pushButton_2.setText(_translate("Help_window", "HELP"))
        self.pushButton_3.setText(_translate("Help_window", "Далее"))
        self.pushButton_4.setText(_translate("Help_window", "Назад"))
        self.tableView.setWhatsThis(_translate("Help_window", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("Help_window", "Примечание"))
        self.pushButton_5.setText(_translate("Help_window", ". . ."))
        
        
    def on_button_click(self, e) :
        folder_path = QFileDialog.getExistingDirectory()
        if folder_path:
            self.textEdit.setText(folder_path)
        
        
    



