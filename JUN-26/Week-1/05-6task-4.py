# T-4 Check for negative even and negative odd.
num = int(input("Enter the number : "))
if (num < 0):
    if(num % 2 == 0):
        print("Number is Negative Even")
    else:
        print("Number is Negative Odd")
else:
    print("Number is Poitive")