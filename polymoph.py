# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

# Subclasses with unique move() implementations
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the clouds ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing across the sea 🚤")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling down the trail 🚴")

# Example usage
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()