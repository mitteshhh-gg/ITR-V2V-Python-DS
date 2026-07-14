# Multiple-Inheritance
class Mother():
    def fun1(self):
        print("Mother Class!")

class Father():
    def fun2(self):
        print("Father Class!")

class Child(Mother,Father):
    def fun3(self):
        print("Child Class!")

c1 = Child()
c1.fun1()
c1.fun2()
c1.fun3()