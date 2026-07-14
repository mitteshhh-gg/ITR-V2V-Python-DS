# Single-Inheritance
class Parent:
    def fun1(self):
        print("Parent Class!")

class Child(Parent):
    def fun2(self):
        print("Child Class!")

p1 = Child()
p1.fun1()
p1.fun2()