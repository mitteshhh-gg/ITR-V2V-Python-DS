# Create another Student object with different details and display its information.
class Student:
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def show_info(self):
        print(f"Name : {self.name} \nAge : {self.age}yrs")
        print(f"Weight : {self.weight}kg \nHeight : {self.height}")

s1 = Student("Mitesh Vaykar",17,45,157)
s1.show_info()
s2 = Student("Arjun Kapoor",18,62,160)
s2.show_info()