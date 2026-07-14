class Rectangle:

    def __init__(self,l,w):
        self.length = l
        self.width = w

    
    def display(self):
        print(f"Dimensions :-")
        print(f"Length : {self.length}\nWidth : {self.width}")

r = Rectangle(15,8)
r.display()


















    # def area(self):
    #     return self.length * self.width
# print(f"Area of Rectangle : {r.area()}")
