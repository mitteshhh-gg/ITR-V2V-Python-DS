class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    
    def display(self):
        print(f"Name of Student : {self.name}")
        print(f"Age : {self.age}")

class Student(Person):
    def __init__(self,n,a,roll,co,ma):
        Person.__init__(self,n,a)
        self.rollNo = roll
        self._course = co
        self.__marks = ma

    def setMarks(self):
        self.__marks = list(input("Enter Marks of 3 Sub : "))

    def getMarks(self):
        print(f"Marks of 3 Subjects Sub : {ma}")
    
    def display(self):
        Person.display(self)
        print(f"Roll No : {self.rollNo}")
        print(f"Course : {self._course}")

class SportStudents(Student):
    def __init__(self, n, a, roll, co, ma, spna):
        Student.__init__(self, n, a, roll, co, ma,)
        self.sportName = spna 
        
    def display(self):        
        Student.display(self)
        print(f"Sport Name : {self.sportName}")

class Result(SportStudents):
    def __init__(self, n, a, roll, co, ma,spna):
        SportStudents.__init__(self, n, a, roll, co, ma, spna)

    def calRes(self,ma):
        self.marks = ma
        total = sum(ma)
        
        per = (total / 300) * 100
        if per >= 90:
            grade = "A"
        elif per >= 75:
            grade = "B"
        elif per >= 50:
            grade = "C"
        else:
            grade = "F"

        print(f"Total Marks : {total}")
        print(f"Percentage : {per}%")
        print(f"Grade : {grade}")

print("--- Enter Student Details ---")
na = input("Enter Name : ")
age = int(input("Enter Age : "))
roll = int(input("Enter Roll No : "))
co = input("Enter Course : ")
# ma = int(input("Enter Marks for 3 Subjects : "))
sport = input("Enter Sport Name : ")

s1 = SportStudents(na,age,roll,co,[],sport)

s1.display()

ma = s1.setMarks()
s1 = SportStudents(na,age,roll,co,[ma],sport)

s1.getMarks()

