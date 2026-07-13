#---Variables---
stdName = "Mitesh Vaykar"
age = 17
marks = 88.59
isPass = True
rollNo = 58
city = "Thane"
totalMarks = 500
course = "Computer Engineering"
#---Invalid Variables---
#1student = "Mitesh Vaykar"         - Can't start variable name with a number
#@marks = 88.59                     - Can't start variable name with a special keyword 
#is-Pass = True                     - Can't use Hyphen (-) in Variable name
#roll No = 58                       - Spaces aren't allowed in-between variable name 
#class = "Computer Engineering"     - class is a reserved python keyword
#---Displaying Variables
print("\nStudent Name : ", stdName)
print("Data Type:", type(stdName))

print("\nAge : ", age)
print("Data Type : ", type(age))

print("\nmarks : ", marks)
print("Data Type : ", type(marks))

print("\nIs pass? : ", isPass)
print("Data Type : ", type(isPass))

print("\nRoll No : ", rollNo)
print("Data Type:", type(rollNo))

print("\nCity Name : ", city)
print("Data Type:", type(city))

print("\nTotal Marks : ", totalMarks)
print("Data Type : ", type(totalMarks))

print("\nCourse : ", course)
print("Data Type : ", type(course))


#Creating and Displaying List, Tuple, and Dictionary
# 1. List : Lists are ordered and mutable (can be modified).
subjects = ["Python", "Java", "C", "DBMS"]
print("\nList : ", subjects)
print("Data-Type : ", type(subjects))

# 2. Tuple : Tuples are ordered and immutable (cannot be modified).
marks = (84, 94, 89, 85, 92)
print("\nTuple : ", marks)
print("Data-Type : ", type(marks))

# 3. Dictionary : Dictionaries store data as key-value pairs.

student = {
    "name": "Mitesh Vaykar",
    "roll_no": 58,
    "course": "Computer Engineering"
}
print("\nDictionary : ", student)
print("Data-Type : ", type(student))

# [] Brackets:
# Used to create a List.

# () Parentheses:
# Used to create a Tuple.

# {} Braces:
# Used to create a Dictionary or Set.

