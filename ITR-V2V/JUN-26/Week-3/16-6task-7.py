#try-except-else-finally stmts
try:
    n = int(input("Enter a number : "))
    res = 100 / n
except ZeroDivisionError:
    print("Error! Division by Zero is Not Possible")
except ValueError:
    print("Error! Value is invalid!")
else:
    print(f"Result = {res}")
finally:
    print("Execution Completed")