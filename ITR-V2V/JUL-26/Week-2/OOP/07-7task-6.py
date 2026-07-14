# prblm stmt-1
class Person():
    def __init__(self,n,a):
        self.name = n
        self.age = a

class Student(Person):
    def __init__(self,n,a,r):
        Person.__init__(self,n,a)
        self.rollno = r

    def show(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Roll No : {self.rollno}")

s1 = Student("Mitesh",17,67)
s1.show()