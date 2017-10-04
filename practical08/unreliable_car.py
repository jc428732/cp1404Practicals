from car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):
        if self.reliability > random.randint(0, 100):
            super().drive(distance)
        return 0
