''' 예제1) lineEdit1에 쓴글자가 lineEdit2에 작성 '''

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

class MyWin:
    def __init__(self):
        self.dlg = loadUi('ui2.ui')
        self.dlg.lineEdit.textChanged.connect(self.txtChange)
        self.dlg.show()

    def txtChange(self):
        get_line1 = self.dlg.lineEdit.text()
        self.dlg.lineEdit_2.setText(get_line1)

'''
    def fn(self):
        # setter
        #print("click....")
        # self.dlg.lineEdit.setText('코리아')

        # getter
        s=self.dlg.lineEdit.text()
        print(s)
'''


app = QApplication(sys.argv)

myWin = MyWin()   # class호출함

app.exec()


