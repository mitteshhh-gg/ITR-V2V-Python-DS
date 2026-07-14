# Q.6

class Principal:
    def manage_school(self):
        print("Hello! I'm the PRINCIPAL and I manage the school")

class Teacher(Principal):
    def teach(self):
        print("Hello I'm a TEACHER and I teach students ")
    
class Student(Principal):
    def study(self):
        print("Hello I'm a STUDENT and I study in school")
    
t1 = Teacher()
s1 = Student()

t1.manage_school()
t1.teach()
s1.study()

