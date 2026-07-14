# Q.7

class Device():
    def Power_on(self):
        print("Power of DEVICE is ON!")
    
class Phone(Device):
    def call(self):
        print("Calling thorugh PHONE")
    
class Camera(Device):
    def take_photo(self):
        print("Taking Photo by CAMERA")

class Smartphone(Phone,Camera):
    pass

s1 = Smartphone()
s1.Power_on()
s1.call()
s1.take_photo()