## PYQT 

### class속성 (3가지)

instance :  self.이름,  instance.이름 

class속성:  class이름   instance.이름 (class.이름 추가지원)
-> 내부에서 차이남 

## 기본 구조 
widge(button,lineEdit) -> layout -> window (Qdialog함수)
이벤트 연결: connect (힘수이름)  

STEP0) app=QApplication(sys.argv)

STEP1) window생성
dlg=QDialog()  #window 생성
dlg.show()     #화면에 보여줌

STEP2) layout생성
vbox=QVBoxLayout()

STEP3)  widget추가 -> layout 등록  
btn = QPushButton('클릭')
btn.clicked.connect(fn)
lineEdit=QLineEdit()

vbox.addWidget(btn)
vbox.addWidget(lineEdit)

STEP4) layout->window
dlg.setLayout(vbox)

SETP6) app.exec()  # 큐메모리 감시 무한 loop


## Class 구조(변경) 
STEP1) class 생성 
- ui + event 
- ui: desinger(xml)대체함 
- event만 만들어주면됨

STEP2) class호출 
app = QApplication(sys.argv)
myWin = MyWin()   # class호출
app.exec()


## Event 
self.dlg.pushButton.clicked.connect(self.fn)   //버턴 클릭 

self.dlg.lineEdit.textChanged.connect(self.txtChange)  //LineEdit 내용변경 



## getter/setter 
-get: GUI에 보이는 변수이름 활용
-set: set+변수이름사용 

-getter : text(), value()
-setter : setText('코리아'), setPixmap(QPixmap(파일이름))


## widget 

### lineEdit 
self.dlg.lineEdit.text()             // get(text가져옴)
self.dlg.lineEdit.setText('코리아')  // setText(set)

### spinbox(숫자)
n1=self.dlg.spinBox.value()     //get (value 가져옴)


### label
self.dlg.label_4.setPixmap(QPixmap('bi01.jpg'))   //setPixmap(set)


### date
self.dlg.dateEdit.setDate(QDate(2022,2,21) )  // 기본값 설정(setter)
 
self.dlg.dateEdit.date()   // getter(class반환) 
s = f'{dt.year()}년 {dt.month()}월 {dt.day()}일'
self.dlg.lineEdit.setText(s)