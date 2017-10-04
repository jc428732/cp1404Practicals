from unreliable_car import UnreliableCar

car = UnreliableCar("Car", 100, 50)
print(car)
for i in range (0, 5):
    car.drive(10)
    print(car)