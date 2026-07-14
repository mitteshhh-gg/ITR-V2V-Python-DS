#3. Write a Python program to implement encapsulation using an "ATM" class with a private "__pin" attribute.
class ATM:
    def __init__(self,name,pin):
        self.name = name
        self.__pin = pin

    def setPin(self):
        print("------------------------------------")
        print("You need to set the pin first!")
        self.__pin = int(input("Enter the pin of  6-digits:"))
        print("Pin Successfully set")
        
    def display(self):
        print("------Details------")
        print(f"Name: {self.name}\nPin is : {self.__pin}")
        print("Pin is set you can use your card")

c1=ATM("Mitesh",0)
c1.setPin()
c1.display()
