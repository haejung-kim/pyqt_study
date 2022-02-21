from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *

import sys

class MyWin:
    def __init__(self):
        self.dlg = loadUi('ui3.ui')
        self.dlg.pushButton.clicked.connect(self.fn)
        self.dlg.show()
    def fn(self):
        self.dlg.labelTest.setPixmap(QPixmap('b.jpg'))

app = QApplication(sys.argv)
myWin = MyWin()
app.exec()
