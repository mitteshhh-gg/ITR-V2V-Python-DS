# Modify the Student class so that the __init__() method also accepts an age parameter and stores it.
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"Hello My name is {self.name} & I'm {self.age} years old")

s1 = Student("Mitesh Vaykar",17)
s1.show_info()