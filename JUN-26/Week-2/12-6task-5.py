# Skip all numbers divisible by 3 between 1 to 10.
i = 0
while (i < 10):
    i += 1
    if (i % 3 == 0):
        continue
    print(i)