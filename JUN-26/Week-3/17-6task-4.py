# Ask the user to enter a number between 1 and 10. Keep retrying if the input is not a number or is out of range.
while True:
    try:
        a = int(input("\nEnter a number between 1-10 : "))

        if a <= 10 and a > 0:
            print(f"The number is : {a}")
            break
        else:
            print("\nError! Enter a number between 1-10")
    except ValueError:
        print("\nInvalid Input! Can't Input Character")
