def add(a,b):
    print(f"Addition of {a} and {b} : {a + b}")
    # return a + b
def sub(a,b):
    print(f"Subtraction of {a} and {b} : {a - b}")
    # return a - b
def mul(a,b):
    print(f"Multiplication of {a} and {b} : {a * b}")
    # return a * b

def div(a,b):
    if b == 0:
        print("Invalid Denominator")
    else:
        print(f"Division of {a} and {b} : {a / b}")
    # return a / b
print("\n---Simple Calculator---")
print("\n1. Addition.")
print("\n2. Subtraction.")
print("\n3. Multiplication.")
print("\n4. Division.")

ch = int(input("Enter your choice : "))
a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))

if (ch == 1):
    add(a,b)
elif(ch == 2):
    sub(a,b)
elif(ch == 3):
    mul(a,b)
elif(ch == 4):
    div(a,b)
else:
    print("Invalid Input!")
