from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

class MyWin:
    def __init__(self):
        self.dlg=loadUi('ui1.ui')
        self.dlg.pushButton.clicked.connect(self.fn)
        self.dlg.lineEdit.textChanged.connect(self.txtChange)
        self.dlg.show()

    def txtChange(self):
        s = self.dlg.lineEdit.text()
        print(s)

    def fn(self):
        # setter
        #print("click....")
        # self.dlg.lineEdit.setText('코리아')

        # getter
        s=self.dlg.lineEdit.text()
        print(s)

app = QApplication(sys.argv)

myWin = MyWin()   # class호출함

app.exec()


