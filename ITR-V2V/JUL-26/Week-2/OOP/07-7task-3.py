#Multilevel-Inheritance
class Grandfather():
    def fun1(self):
        print("Class of Grandfather")

class Parent(Grandfather):
    def fun2(self):
        print("Class of Parent")

class Child(Parent):
    def fun3(self):
        print("Class of Child")

c1 = Child()
c1.fun1()
c1.fun2()
c1.fun3()

