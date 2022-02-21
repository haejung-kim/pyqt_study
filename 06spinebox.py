from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

class MyWin:
    def __init__(self):
        self.dlg = loadUi('ui2.ui')
        self.dlg.pushButton.clicked.connect(self.fn)
        self.dlg.show()

    def fn(self):
        n1=self.dlg.spinBox.value()
        n2=self.dlg.spinBox_2.value()
        print(n1,n2, n1+n2)
        self.dlg.lineEdit.setText(f'합은:{n1+n2}')
app = QApplication(sys.argv)
myWin = MyWin()
app.exec()
