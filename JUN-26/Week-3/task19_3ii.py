# Create a new module with a function that returns the square of a num.Use it in another file.
import task19_3i as sqr

num = int(input("Enter the number for square : "))
print(f"Square of {num} = {sqr.sq(num)}")