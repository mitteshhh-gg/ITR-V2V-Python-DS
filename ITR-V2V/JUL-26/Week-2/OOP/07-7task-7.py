# problem stmt-2
class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    def drive(self):
        print("Car is being driven")

c1 = Car()
c1.start()
c1.drive()