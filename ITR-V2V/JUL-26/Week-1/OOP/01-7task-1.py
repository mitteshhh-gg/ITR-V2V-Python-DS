# Create a second Student object with a different name and make it say hello.
class Student:
    def set_name(self,name):
        self.name = name

    def say_hello(self):
        print(f"Hello! My name is {self.name}")

s1 = Student()
s1.set_name("Mitesh Vaykar")
s1.say_hello()
s2 = Student()
s2.set_name("Smaran Borse")
s2.say_hello()
