#function with parameters
def add(a,b):
    print(f"Addition of {a} and {b} : {a + b}")
def sub(a,b):
    print(f"Subtraction of {a} and {b} : {a - b}")
def mul(a,b):
    print(f"Multiplication of {a} and {b} : {a * b}")
def div(a,b):
    if b == 0:
        print("Invalid Denominator")
    else:
        print(f"Division of {a} and {b} : {a / b}")
print("\n---Simple Calculator---")
a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))

add(a,b)
sub(a,b)
mul(a,b)
div(a,b)
