from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from cnc_gui import Ui_MainWindow

class Prog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.printBtn.clicked.connect(self.printFunction)
        self.ui.clearBtn.clicked.connect(self.clearFunction)

    def printFunction(self):
        self.ui.textEdit.setPlainText('hello, world\n')
        print('hello, world')

    def clearFunction(self):
        self.ui.textEdit.setPlainText('')

if __name__=='__main__':
    app =  QtWidgets.QApplication(sys.argv)
    win = Prog()
    win.show()
    sys.exit(app.exec_())