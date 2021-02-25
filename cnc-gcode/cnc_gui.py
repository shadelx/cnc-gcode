# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cnc-gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileLabel = QtWidgets.QLabel(self.centralwidget)
        self.fileLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Ubuntu Condensed\";\n"
"color: rgb(46, 52, 54);")
        self.fileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fileLabel.setObjectName("fileLabel")
        self.horizontalLayout.addWidget(self.fileLabel)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.selectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Ubuntu Condensed\";")
        self.selectBtn.setObjectName("selectBtn")
        self.horizontalLayout.addWidget(self.selectBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 13pt \"Ubuntu\";\n"
"")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Ubuntu Condensed\";")
        self.clearBtn.setObjectName("clearBtn")
        self.verticalLayout_3.addWidget(self.clearBtn)
        self.printBtn = QtWidgets.QPushButton(self.centralwidget)
        self.printBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Ubuntu Condensed\";")
        self.printBtn.setObjectName("printBtn")
        self.verticalLayout_3.addWidget(self.printBtn)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "cnc pint"))
        self.fileLabel.setText(_translate("MainWindow", "select a file"))
        self.selectBtn.setText(_translate("MainWindow", "select"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">[+ ]Welcome to this program</span></p></body></html>"))
        self.clearBtn.setText(_translate("MainWindow", "clear"))
        self.printBtn.setText(_translate("MainWindow", "print"))
