# Hierarchy
class Parent():
    def fun1(self):
        print("Class of Parent")
class Child1(Parent):
    def fun2(self):
        print("Class of Child 1")
class Child2(Parent):
    def fun3(self):
        print("Class of Child 2")

c1 = Child1()
c1.fun1()
c1.fun2()

c2 = Child2()
c2.fun1()
c2.fun3()