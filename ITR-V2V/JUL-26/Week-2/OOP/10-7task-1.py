# Q.1
from abc import ABC,abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.14*self.radius*self.radius
    
c1 = Circle(3)
print(f"Area is : {c1.area()}") 