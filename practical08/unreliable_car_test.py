from unreliable_car import UnreliableCar

car = UnreliableCar("Car", 1000000, 50)
print(car)
successes = 0
total_attempts = 0
for i in range(0, 1000):
    print(car.drive(1))
    distance = 0
    if distance > 0:
        successes += 1
    total_attempts += 1
    print(car)
print(successes / total_attempts)