# Add an age attribute using a method and modify say_hello() to include the student's age.
class Student:
    def set_name(self,name):
        self.name = name

    def set_age(self,age):
        self.age = age

    def say_hello(self):
        print(f"Hello! My name is {self.name} & I'm {self.age} years old")

s1 = Student()
s1.set_name("Mitesh Vaykar")
s1.set_age(17)
s1.say_hello()
