# Catch non-integer inputs and print *"Invalid input"* if the user enters letters.
try:
    a = int(input("Enter a number : "))
    print(f"You Entered : {a}")

except ValueError:
    print("Invalid Input! Can't Input Character")
