from car import Car
from random import randint

class UnreliableCar(Car):
    """Inherit from car object but less reliable."""
    MINIMUM_DRIVE_CHANCE = 0
    MAXIMUM_DRIVE_CHANCE = 100

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance.

        reliability: float, determines how often car will drive
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car if the chance is less than the car's reliability.'"""
        if randint(self.MINIMUM_DRIVE_CHANCE, self.MAXIMUM_DRIVE_CHANCE) < self.reliability:
            super().drive(distance)
        return 0
