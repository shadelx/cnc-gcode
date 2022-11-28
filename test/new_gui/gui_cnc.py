# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_cnc.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import serial as ser
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 354)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.file_label = QtWidgets.QLabel(self.centralwidget)
        self.file_label.setObjectName("file_label")
        self.horizontalLayout_2.addWidget(self.file_label)
        self.upload_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.upload_btn.setFont(font)
        self.upload_btn.setStyleSheet("QPushButton\n"
"{\n"
"  display: inline-block;\n"
"  padding: 15px 25px;\n"
"  font-size: 10px;\n"
"  cursor: pointer;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color: #4CAF50;\n"
"  border: none;\n"
"  box-shadow: 0 9px #999;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#3e8e41;\n"
"}")
        self.upload_btn.setObjectName("upload_btn")
        self.horizontalLayout_2.addWidget(self.upload_btn)
        self.clr_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.clr_btn.setFont(font)
        self.clr_btn.setStyleSheet("QPushButton\n"
"{\n"
"  display: inline-block;\n"
"  padding: 15px 25px;\n"
"  font-size: 10px;\n"
"  cursor: pointer;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color: #4CAF50;\n"
"  border: none;\n"
"  box-shadow: 0 9px #999;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#3e8e41;\n"
"}")
        self.clr_btn.setObjectName("clr_btn")
        self.horizontalLayout_2.addWidget(self.clr_btn)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet("background-color: #4CAF50;\n"
"text-align: center;\n"
"line-height: 30px;\n"
"color: white;\n"
"")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.print_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.print_btn.setFont(font)
        self.print_btn.setStyleSheet("QPushButton\n"
"{\n"
"  display: inline-block;\n"
"  padding: 15px 25px;\n"
"  font-size: 14px;\n"
"  cursor: pointer;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color: #4CAF50;\n"
"  border: none;\n"
"  box-shadow: 0 9px #999;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#3e8e41;\n"
"}")
        self.print_btn.setObjectName("print_btn")
        self.horizontalLayout.addWidget(self.print_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("QPushButton\n"
"{\n"
"  display: inline-block;\n"
"  padding: 15px 25px;\n"
"  font-size: 14px;\n"
"  cursor: pointer;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color: #4CAF50;\n"
"  border: none;\n"
"  box-shadow: 0 9px #999;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#3e8e41;\n"
"}")
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.textEdit.insertPlainText("*****Welcome to ink program*****\n\n\n")

        self.serial_connection()  # star serial connection
        time.sleep(2)
        self.arduino_read()
        self.initial_configuration()
        self.clr_btn.clicked.connect(self.clear_text)
        self.upload_btn.clicked.connect(self.upload_file)
        self.print_btn.clicked.connect(self.print_file)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ink print"))
        self.file_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">hello.pdf                   </span></p></body></html>"))
        self.upload_btn.setText(_translate("MainWindow", "Upload"))
        self.clr_btn.setText(_translate("MainWindow", "Clear"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.print_btn.setText(_translate("MainWindow", "Imprimir"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancelar"))
        
    def serial_connection(self):
        try:
            port = '/dev/ttyUSB0'
            baudrate = 115200
            time = .1
            self.arduino = ser.Serial(port,baudrate,timeout=time)
            self.textEdit.insertPlainText('connection succesfully\n')
            self.arduino.write(str.encode('$\n'))
        except:
            self.textEdit.insertPlainText('and error has ocurred, serial connection unsuccesfully\n')

    def arduino_read(self):
        flag =True

        while True and flag == True:
                output =self.arduino.readline()
                if output:              #optuvo una lectura positiva
                        self.textEdit.insertPlainText(output.decode().strip()+'\n')
                else :
                        flag =False  

    def initial_configuration(self):
        try:
                self.arduino.write(str.encode("G10 P0 L20 X0 Y0 Z0")) #define zero
                self.textEdit.insertPlainText("configuracion inicial correcta\n")
        except:
                self.textEdit.insertPlainText("errore en configuracion inicial\n")

    def clear_text(self):
        self.textEdit.clear()
    
    def upload_file(self):
       # filter_file = 'pdf(*.pdf)'
        file_path = QFileDialog.getOpenFileName(None, '/home/zai/Dropbox/cnc/coding/extra/')
        self.textEdit.insertPlainText("file uploaded: {} \n".format(file_path))
        print(type(file_path))
        print(file_path)
        file_real_path = file_path[0]
        print(file_real_path)
        type(file_real_path)
        self.file_label.setText(file_real_path)

        self.file_path = file_real_path

    def print_file(self):
        print(self.file_path)
        file_extension = self.file_path[-3:]
        print(file_extension)

        if file_extension =='pdf':
                file_output = self.file_path[:-3]+'gcode'
                print(file_output)
                try:
                        os.system('pstoedit -f gcode {} {}'.format(self.file_path,file_output))
                        self.textEdit.insertPlainText('conversion exitosa\n')
                        self.textEdit.insertPlainText('archivo codigo G:'+file_output+'\n')
                except:
                        self.textEdit.insertPlainText('error en conversion de archivo\n')

                try:
                        f = open(file_output, 'r')
                        print("archivo abierto")
                except:
                        self.textEdit.insertPlainText('error de apertura de documento G-Code\n')

                try:
                        for line in f:
                                l = line.strip()
                                self.arduino.write(str.encode(l+'\n'))
                                self.textEdit.insertPlainText("printing:"+l+'\n')
                                #grbl_out=self.arduino.readline()
                                #self.textEdit.insertPlainText(grbl_out.decode().strip+'\n')

                        self.textEdit.insertPlainText("print complete")
                        f.close()
                except:
                        self.textEdit.insertPlainText("error en la impresion del G-Code\n")
        else:
                try:
                        f = open(self.file_path, 'r')
                        print("file open")
                        for line in f:
                                l = line.strip()
                                self.arduino.write(str.encode(l+'\n'))
                                self.textEdit.insertPlainText("printing:"+l+'\n')
                                #grbl_out=self.arduino.readline()
                                #self.textEdit.insertPlainText(grbl_out.decode().strip+'\n')
                        self.textEdit.insertPlainText("print complete")
                        f.close()
                except:
                        self.textEdit.insertPlainText("error en la impresion del G-Code\n")
        
    def cancelar(self):
        try:
                self.arduino.write(str.encode("G21 G90 G0Z5\nG90 G0 X0 Y0\nG90 G0 Z0\n")) #define zero
                self.textEdit.insertPlainText("proyecto cancelado\n")
        except:
                self.textEdit.insertPlainText("error en la cancelacion\n")   
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    MainWindow.arduino.close()
