# Q.2
class Animal:
    
    def speak(self):
        print("Class Animal")

class Bird(Animal):
    
    def speak(self):
        print("Tweet!")

b = Bird()
b.speak()
