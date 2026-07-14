#Write a Python program to create a "Student" class with a private "__marks" attribute and a method to display marks
class Student:
    def __init__(self,marks,name):
        self.__marks=marks
        self.name=name

    def show(self):
        print(f"Marks : {self.__marks}")

s1=Student(85,"Mitesh")
print(f"Name : {s1.name}")
s1.show()
