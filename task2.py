class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving 🚗.")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying ✈️.")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing 🚤.")

class Bicycle(Vehicle):
    def move(self):
        print(f"{self.name} is cycling 🚲.")


car = Car("Toyota")
plane = Plane("Boeing 747")
boat = Boat("Sailboat")
bicycle = Bicycle("Mountain Bike")

vehicles = [car, plane, boat, bicycle]

for vehicle in vehicles:
    vehicle.move()
