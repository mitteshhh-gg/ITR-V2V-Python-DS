#Exception Handling
#Error Handling using -> try-except
try:
    num = int(input("Enter number :  "))
    print(10 / num)

except ZeroDivisionError:
    print("Error! Division by Zero is Not Possible")
    