# Create a new Car object (e.g., car3 = Car("green")) and print car3.color and Car.wheels.
class Car:
    wheels = 4

    def __init__(self,color):
        self.color = color

car1 = Car("White")
car2 = Car("Yellow")

print(f"Color of Car2 : {car2.color}\nNumber of wheels : {Car.wheels}")
print(f"Color of Car1 : {car1.color}\nNumber of wheels : {Car.wheels}")