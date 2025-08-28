# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and I wield the power of {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power} to save the day!")

# Subclass with added attributes and polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} soars through the skies at {self.flight_speed} km/h using {self.power}!")

# Another subclass
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadgets):
        super().__init__(name, power, origin)
        self.gadgets = gadgets

    def use_power(self):
        print(f"{self.name} deploys {', '.join(self.gadgets)} to outsmart the villains!")

# Example usage
falcon = FlyingHero("Falcon Blaze", "Wind Manipulation", "Sky Realm", 800)
falcon.introduce()
falcon.use_power()

cyber = TechHero("Cyber Nova", "Tech Genius", "Neo City", ["Drone Swarm", "EMP Blaster"])
cyber.introduce()
cyber.use_power()
