# Use pass with multiple conditions.
a = 20

if a > 0 and a % 2 == 0:
    pass   
elif a > 0 and a % 2 != 0:
    pass   
elif a < 0:
    pass   
else:
    pass   
print("Condition check completed")