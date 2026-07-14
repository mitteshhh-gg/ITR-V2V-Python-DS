# Method Overloading

class Example:
    def add(self,a, b):
        x = a + b
        return x

    def add(self,a, b, c):
        x = a + b + c
        return x
    
e1 = Example()

print(e1.add(4, 5, 6))
print(e1.add(4, 5))