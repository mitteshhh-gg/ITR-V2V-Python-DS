#variables
name = "Mitesh Vaykar"
age = 17
clg_name = "Goverment Polytechnic, Thane"
percentage = 87.65

#displaying along with their data-type
print("Name : ", name)
print("Data-Type of Name : " ,type(name))

print("\nAge : ", age)
print("Data-Type of Age : " ,type(age))

print("\nCollege Name : ", clg_name)
print("Data-Type of College Name : " ,type(clg_name))

print("\nPercentage : ", percentage)
print("Data-Type of Percentage : " ,type(percentage))

#type-conversion
age = float(age)
print("\nAge : ", age)
print("Data-Type of Age After Conversion : ", type(age))

percentage = int(percentage)
print("\nPercentage : ", percentage)
print("Data-Type of Percentage After Conversion : ", type(percentage))
