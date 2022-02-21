class Test:
    count=0   # class변수

    def __init__(self, x, y):
        print('init call')
        self.a = x
        self.b = y
        self.__c = 100   # private 속성 
        Test.count+=1    # class속성 

    def setData(self, x, y):
        self.a = x
        self.b = y

    def show(self):
        print(self.a)
        print(self.b)

obj= Test(10,20)
obj2= Test(30,40)

obj.setData(100,200)
obj.show()

print(obj.count)
print(Test.count)

# private 속성 
print(obj._Test__c)  #  _클래스이름__변수 