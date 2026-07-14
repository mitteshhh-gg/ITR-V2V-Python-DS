# Q.4

class Flyer:
    def fly(self):
        print("Look I can Fly this HIGH!")
class Swimmer:
    def swim(self):
        print("Look I can Swim this DEEP!")

class FlyingFish(Flyer,Swimmer):
    pass

f1 = FlyingFish()
f1.fly()
f1.swim()