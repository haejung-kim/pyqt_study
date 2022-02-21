from PyQt5.QtWidgets import *
import sys

'''
변수명: self 
함수 인자(self)
함수 호츨(self.fn)

구성 
1) class생성 
2) app = QApplication(sys.argv)
3) myWin = MyWin() -> class호출
3) app.exec()

'''

class MyWin:
    def __init__(self):
        self.dlg = QDialog()
        self.dlg.setWindowTitle('다이아로그')
        self.dlg.setGeometry(100,100, 500,500)
        self.vbox = QVBoxLayout()
        self.btn = QPushButton('클릭')
        self.btn.clicked.connect(self.fn) #event 등록.
        self.lineEdit = QLineEdit()
        self.vbox.addWidget(self.btn)
        self.vbox.addWidget(self.lineEdit)
        self.dlg.setLayout(self.vbox)
        self.dlg.show()

    def fn(self):
        print("click....")

app = QApplication(sys.argv)

myWin = MyWin()   # class호출함

app.exec()


# self.dlg=QDialog()
# self.dlg.setWindowTitle('다이아로그')
# self.dlg.lineEdit = QLineEdit()
# self.dlg.pushButton = QPushButton()

