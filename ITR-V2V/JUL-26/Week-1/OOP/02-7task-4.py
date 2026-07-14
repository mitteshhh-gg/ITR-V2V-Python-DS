class Employee:
    def __init__(self,n,a):
        self.name = n            #public
        self._age = a            #protected

class SubEmp(Employee):
    def showAge(self):
        print(f"Age : {self._age}")

emp = SubEmp("Mitesh",19)
print(f"Name : {emp.name}")
emp.showAge()