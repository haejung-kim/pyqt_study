from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MyWin:
    def __init__(self):
        self.dlg = loadUi('파일명.ui')
        #self.dlg.pushButton.clicked.connect(self.fn)
        self.dlg.show()

    def fn(self):
        print('test')

app = QApplication( sys.argv)
myWin = MyWin()
app.exec()
