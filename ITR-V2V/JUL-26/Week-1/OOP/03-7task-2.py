#2. Create an "Employee" class with a private "__salary" attribute and methods to update and display the salary.
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def UpdateSal(self):
        print("--------------------------------------")
        print(f"Current salary is : {self.__salary}")
        self.__salary=int(input("Enter New Salary:"))
        print("--------------------------------------------")

    def display(self):
        print("--------Employee Details-------")
        print(f"Name : {self.name}")
        print(f"New Salary is : {self.__salary}")

e1=Employee("Mitesh",45000)
e1.UpdateSal()
e1.display()
