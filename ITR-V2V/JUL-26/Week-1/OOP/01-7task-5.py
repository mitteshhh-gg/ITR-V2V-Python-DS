class Bike:
    wheels = 2
    def __init__(self,color):
        self.color = color
        print(f"Bike-1 :\nNumber of wheels : {self.wheels}.\nColor of Bike : {self.color}.")

b1 = Bike("Red")
