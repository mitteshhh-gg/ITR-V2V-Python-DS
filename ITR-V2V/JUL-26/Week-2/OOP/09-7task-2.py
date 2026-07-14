# Method Overriding
class Parent:
    def MyMethod(self):
        print("Calling Parent Method")

class Child(Parent):
    def MyMethod(self):
        print("Calling Child Method")

c = Child()         #Creating Object

c.MyMethod()        #Calling Method which is Overridden

