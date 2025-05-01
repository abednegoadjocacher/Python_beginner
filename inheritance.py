# Inheritance in python: Is when one class has inherit methods or attributes from the parent class

class Car:
    def drive(self):
        print("Drive the car")

class Audi(Car): #The base class Car is passed to the child class.
    def pack(self):
        print("I love coding")


car_1 = Audi()
car_1.drive()
car_1.pack()