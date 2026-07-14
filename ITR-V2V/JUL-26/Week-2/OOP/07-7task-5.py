# Hybrid Inheritance
class Parent():
    def fun1(self):
        print("Class of Parent")

class Child1(Parent):                   
    def fun2(self):
        print("Class of Child 1")

class Child2(Parent):
    def fun3(self):
        print("Class of Child 2")

class Child3(Child1,Child2):
    def fun4(self):
        print("Class of Child 3")

c1 = Child3()
c1.fun1()
c1.fun2()
c1.fun3()
c1.fun4()
