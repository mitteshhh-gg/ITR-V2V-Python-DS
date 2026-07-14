# Duck Typing
class Duck:
    def sound(self):
        print("Quack! Quack!")
    
class AnotherBird:
    def sound(self):
        print("I'm similar to a Duck")
    
def makeSound(bird):
    bird.sound()

duck = Duck()
anotherBird = AnotherBird()

makeSound(duck)
makeSound(anotherBird)
