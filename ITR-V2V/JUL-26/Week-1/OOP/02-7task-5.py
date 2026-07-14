class Employee:
    def __init__(self,n,s):
        self.name = n            #public
        self.__sal = s           #private
    def showSal(self):
        print(f"Salary : {self.__sal}")

emp = Employee("Mitesh",65000)
print(emp.name)
emp.showSal()
# print(f"{emp.__sal}")         #throws error (private member can't be accessed directly)