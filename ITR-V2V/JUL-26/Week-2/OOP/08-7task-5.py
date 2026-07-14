# Q.5

class Manager:
    def __init__(self, n):
        self.name = n
    
    def greet(self):
        print(f"Hello! This is Manager {self.name}")
        
class Director(Manager):
    def greet(self):
        print(f"Hello! This is Director {self.name}")

d = Director("Mahesh Bhatt")

d.greet()