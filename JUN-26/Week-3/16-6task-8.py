#exception handling with loop
while True:
    try:
        num = int(input("Enter the number : "))
        print(f"You Entered : {num}")
        break
    except ValueError:
        print("Invalid Input!")
