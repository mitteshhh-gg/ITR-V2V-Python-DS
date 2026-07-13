# Add a finally block to print *"Operation complete"* no matter what happens.
try:
    a = int(input("Enter a number : "))
    if a % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
except ValueError:
    print("Invalid Input! Can't Input Character")
finally:
    print("Operation complete!")