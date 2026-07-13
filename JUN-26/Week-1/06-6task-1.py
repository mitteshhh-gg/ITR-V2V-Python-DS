# Task - Creating a simple Calculator where the user will select the operations and on 
# selecting then user will input the values and on enterint it will show the output 

print("\n---Simple Calculator---\n1.Addition.\n2.Subtraction.\n3.Multiplication.\n4.Division")
print("\n---------------------------------------")
ch = int(input("Enter your choice (1-4) : "))
if (ch > 4 or ch < 0):
    print("Option is not available!")
elif (ch == 1):
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd number : "))
    print("Addition of ",a," + ",b," = ", a+b)
elif (ch == 2):
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd number : "))
    print("Sutraction of ",a," - ",b," = ", a-b)
elif (ch == 3):
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd number : "))
    print("Multiplication of ",a," * ",b," = ", a*b)
elif (ch == 4):
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd number : "))
    print("Division of ",a," / ",b," = ", a/b)
else:
    print("Invalid input!")