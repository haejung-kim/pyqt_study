from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
import sys

class MyWin:
    def __init__(self):
        self.dlg = loadUi('ui4.ui')
        self.dlg.pushButton.clicked.connect(self.fn)
        self.dlg.show()

    def fn(self):
        #setter
        #self.dlg.dateEdit.setDate( QDate(2022,2,21) )

        # getter
        dt = self.dlg.dateEdit.date()        #Class를 return함
        s = f'{dt.year()}년 {dt.month()}월 {dt.day()}일'
        self.dlg.lineEdit.setText(s)
app = QApplication( sys.argv)
myWin = MyWin()
app.exec()
