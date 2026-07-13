# Write a program to divide 100 by a user-input number. Handle both zero and non-integer inputs.
try:
    a = int(input("Enter the number : "))
    res = 100 / a
    print(f"Result : {res}")
except ZeroDivisionError:
    print("Can't Divide Number By Zero!")
except ValueError:
    print("Invalid Input! Can't Input Character")

    