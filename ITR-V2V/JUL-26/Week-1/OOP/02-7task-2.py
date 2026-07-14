class Std:
    def __init__(self,n,r):
        self.name = n
        self.rollNo = r

    def percentage(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.per = ((m1+m2+m3) / 300) * 100

    def display(self):
        print("\n---Student Details---")
        print(f"Name : {self.name}.\nRoll No : {self.rollNo}.")
        print(f"Marks of Subjects - ")
        print(f"Subjet 1 : {self.m1}\nSubject 2 : {self.m2}\nSubject 3 : {self.m3}")
        print(f"Percentage : {self.per}")

name = input("Enter Name : ")
rollNo = input("Enter Roll No : ")

m1 = float(input("Enter Marks of Subject 1 : "))
m2 = float(input("Enter Marks of Subject 2 : "))
m3 = float(input("Enter Marks of Subject 3 : "))

s1 = Std(name,rollNo)
s1.percentage(m1,m2,m3)
s1.display()