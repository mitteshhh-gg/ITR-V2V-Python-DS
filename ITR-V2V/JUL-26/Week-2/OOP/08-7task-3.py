# Q.3

class Person():
    def greet(self,name):
        self.name = name
        print(f"Hello! My Name is : {self.name}")
class Teacher(Person):
    def teach(self,prof):
        self.prof = prof
        print(f"My Proffesion is : {self.prof}")

t1 = Teacher()
t1.greet("Samay Rane")
t1.teach("Teacher")