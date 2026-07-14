class Employee:
    def __init__(self,n,s):
        self.name = n            #public
        self.__sal = s           #private

emp = Employee("Mitesh",45000)
print(f"Name : {emp.name}")
# print(f"Name : {emp.__sal}")      #throws error (can't access private member)
