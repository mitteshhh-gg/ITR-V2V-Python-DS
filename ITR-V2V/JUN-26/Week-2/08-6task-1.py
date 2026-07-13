python = int(input("Enter Marks of Python : "))
dbms = int(input("Enter Marks of DBMS : "))
micro = int(input("Enter Marks of Microprocessor : "))

total = python + dbms + micro
avg = float((python + dbms + micro) / 3)

print("\nTotal Marks of Student : ", total)
print("\nAverage : ", avg)
if (avg > 100 or avg < 0):
    print("invalid input!")
elif avg >= 90:
    print("\nGrade of Student : A ")
elif avg >= 80:
    print("\nGrade of Student : B ")
elif avg >= 70:
    print("\nGrade of Student : C ")
elif avg >= 60:
    print("\nGrade of Student : D ")
elif avg >= 50:
    print("\nGrade of Student : E ")
elif avg >= 40:
    print("\nGrade of Student : F ")
else:
    print("Fail!")

