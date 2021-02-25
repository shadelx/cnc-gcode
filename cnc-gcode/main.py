from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from cnc_gui import Ui_MainWindow

class Prog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def printFunction(self):
        pass

if __name__=='__main__':
    app =  QtWidgets.QApplication(sys.argv)
    win = Prog()
    win.show()
    sys.exit(app.exec_())