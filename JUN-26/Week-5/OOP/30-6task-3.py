class Std:

    def set_name(self,name):
        self.name = name

    def say_hello(self):
        print(f"Hello, My name is {self.name}")

s1 = Std()
s1.set_name("Lawrence")
s1.say_hello()