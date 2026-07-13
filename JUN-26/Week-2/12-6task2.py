# Print all numbers from 1 to 20 except multiples of 3. 
for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)
