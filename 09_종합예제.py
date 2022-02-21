from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math
import sys

class MyWin:
    def __init__(self):
        self.dlg = loadUi('ui5.ui')
        self.dlg.pushButton.clicked.connect(self.fn)
        self.dlg.show()

    def biman_decide(self,biman_rate,height,weight) :
        if (biman_rate <= 90):
            self.dlg.lineEdit.setText(f'''
            키:{height} \n
            몸무게:{weight}
            비만: 저체중
                ''')
            self.dlg.label_4.setPixmap(QPixmap('bi01.jpg'))

        elif(biman_rate<=110):
            self.dlg.lineEdit.setText(f'''
            키:{height} \n
            몸무게:{weight}
            비만: 정상
                ''')
            self.dlg.label_4.setPixmap(QPixmap('bi02.jpg'))

        elif (biman_rate <= 120):
            print("3")
            self.dlg.lineEdit.setText(f'''
            키:{height}
            몸무게:{weight}
            비만: 과체중
                ''')
            self.dlg.label_4.setPixmap(QPixmap('bi03.jpg'))
        else:
            print("3")
            self.dlg.lineEdit.setText(f'''
            키:{height}
            몸무게:{weight}
            비만: 비만
                ''')
            self.dlg.label_4.setPixmap(QPixmap('bi04.jpg'))

    def fn(self):
        height = self.dlg.spinBox.value()
        weight = self.dlg.spinBox_2.value()
        st_weight  = (height-100) * 0.85
        biman_rate = math.floor(weight / st_weight * 100)
        print(f'height:{height},weight:{weight}')
        print(f'st_weight:{st_weight},biman_rate:{biman_rate}')
        print(biman_rate,height,weight)
        self.biman_decide(biman_rate,height,weight)


app = QApplication(sys.argv)
myWin = MyWin()
app.exec()
