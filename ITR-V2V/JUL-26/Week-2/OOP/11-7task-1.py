class Person:
    def __init__(self, na, a):
        self.na = na
        self.a = a

    def display(self):
        print("\n--- Personal Details ---")
        print(f"Name : {self.na}")
        print(f"Age : {self.a}")

    # Method Overloading By Different Parameters
    def methOver(self, name, age = None):           
        if age == None:
            print("Name :", name)
        else:
            print("Name :", name)
            print("Age :", age)

class Student(Person):
    def __init__(self, na, a, roll, co):
        Person.__init__(self, na, a)
        self.rollNo = roll
        self._course = co
        self.__marks = []

    # Setter
    def setMarks(self):
        m1 = int(input("Enter Marks of Subject 1 : "))
        m2 = int(input("Enter Marks of Subject 2 : "))
        m3 = int(input("Enter Marks of Subject 3 : "))
        self.__marks = [m1, m2, m3]

    # Getter 
    def getMarks(self):
        return self.__marks     # *

    def display(self):
        Person.display(self)
        print("\n--- Academic Details ---")
        print(f"Roll No : {self.rollNo} " )
        print(f"Course : {self._course} " )


# Multilevel Inheritance
class SportsStudent(Student):
    def __init__(self, na, a, roll, co, sp):
        Student.__init__(self, na, a, roll, co)
        self.sportName = sp

    # Method Overriding
    def display(self):
        Student.display(self)
        print("Sport Name of Student : ", self.sportName)

class Result:
    def calRes(self, ma):
        to = sum(ma)
        per = to / 3

        if per >= 90:
            gr = "A"
        elif per >= 75:
            gr = "B"
        elif per >= 50:
            gr = "C"
        else:
            gr = "F"

        print("\n--- Student Result ---")
        print(f"Marks : {ma}")
        print(f"Total : {to}")
        print(f"Percentage :{per:.2f}%")        # *
        print(f"Grade : {gr}")

print("-------- Student Details --------")
na = input("Enter Name : ")
a = int(input("Enter Age : "))
roll = int(input("Enter Roll No : "))
co = input("Enter Course : ")
sp = input("Enter Sport Name : ")

ss1 = SportsStudent(na, a, roll, co, sp)

ss1.setMarks()              # Setter Method (Encapsulation)
ss1.display()               # Method Overriding

ma = ss1.getMarks()         # Getter Method (Encapsulation)
print("Marks of Student : ", ma)        # *

r1 = Result()               # Display Result
r1.calRes(ma)

print("--- Accessing Student Class 'display' Function ---")
s1 = Student(na,a,roll,co)  
s1.display()                # Display Function of Student Class

print("\n--- Method Overloading ---")
p1 = Person(na,a)
p1.methOver(na)             # * Passing Only 1 Parameter
p1.methOver(na,a)           # * Passing both Parameters





