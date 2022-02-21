class Pet:
    def sleep (self):
        print('sleep')

    def eat(self):
        print('....')


class Dog(Pet) :
    def speak(self):
        print("bow wow")

class Cat(Pet):
    def Speak(self):
        print("meow")

    def Eat(self):  # 오버라이딩(재정의)
        print("fish")

dog=Dog()
dog.sleep()
dog.speak()
dog.eat()

print("----cat----")
cat = Cat()
cat.eat()
