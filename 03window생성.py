from PyQt5.QtWidgets import *
import sys
app=QApplication(sys.argv)

# Window 생성
dlg=QDialog()  #window 생성
dlg.setWindowTitle("다이아로그")
dlg.setGeometry(100,100,1000,700)


# layout생성
vbox=QVBoxLayout()

# (재료:Pushbutton, LineEdit)
btn = QPushButton('클릭')
lineEdit=QLineEdit()

# 재료 > layout 추가(addWidget)
vbox.addWidget(btn)
vbox.addWidget(lineEdit)

# layout->window에 담기(setLayout)
dlg.setLayout(vbox)


dlg.show()     #화면에 보여줌

app.exec()  # 큐메모리 감시 무한 loop
print('hello')  # 하단이라서 실행안됨