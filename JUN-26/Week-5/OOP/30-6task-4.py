class Person:

    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def show(self):
        print(f"Name of the person is : {self.name}  \nAge : {self.age}")

p1 = Person("Osama Bin Laden", 45) 
p2 = Person("Priya" , 30)
p1.show()
p2.show()