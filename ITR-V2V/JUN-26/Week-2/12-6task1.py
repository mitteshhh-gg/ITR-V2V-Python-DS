# Find first number divisible by both 3 and 5 from 1 to 50.
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
            print("First divisible number by both 3 & 5 : ",i)
            break
