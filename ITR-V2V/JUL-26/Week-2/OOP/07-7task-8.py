# prblm stmt-3
class Person:
    def __init__(self):
        self.PerName = "Samay Rane"

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        self.rollno = 21

class Employee(Person):
    def __init__(self):
        Person.__init__(self)
        self.EmpId = 101

class TeachingAssistant(Student, Employee):
    def __init__(self, ta, d, r, empid):
        Student.__init__(self)
        Employee.__init__(self)
        self.Teaname = ta
        self.Teadept = d
    
    def display(self):
        
        print(f"Name of Assistant : {self.Teaname}")
        print(f"Student Roll No : {self.rollno}")
        print(f"Employee ID : {self.EmpId}")
        print(f"Dept of Assistant : {self.Teadept}")


t1 = TeachingAssistant("Samay Rane","IT",67,101)
t1.display()
