from practical08.unreliable_car import UnreliableCar

car = UnreliableCar("Car", 1000000, 50)
print(car)
successes = 0
total_attempts = 1000
for i in range(0, total_attempts):
    distance = car.drive(1)
    if distance > 0:
        successes += 1
    print(car)
print(successes / total_attempts)