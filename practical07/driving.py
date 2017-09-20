from practical07.car import Car

print("Let's drive!")
vehicle = Car(100, str(input("Enter your car name: ")))
print("{}, fuel={}, odo={}".format(vehicle.name, vehicle.fuel, vehicle.odometer))
print("Menu\nd) drive\nr) refuel\nq) quit")
user_choice = str(input("Enter your choice: ")).lower()
while user_choice != "q":
    if user_choice == "d":
        try:
            distance = float(input("How many km do you wish to drive? "))
            while distance < 0:
                print("Distance must be >= 0")
                distance = float(input("How many km do you wish to drive? "))
            distance = vehicle.drive(distance)
            if vehicle.fuel > 0:
                print("The car drove {}km.\n".format(distance))
            else:
                print("The car drove {}km and ran out of fuel.\n".format(distance))
        except TypeError:
            print("Invalid choice\n")
    elif user_choice == "r":
        try:
            fuel_to_add = float(input("How many units of fuel do you want to add to the car? "))
            while fuel_to_add < 0:
                print("Fuel amount must be >= 0")
                fuel_to_add = float(input("How many units of fuel do you want to add to the car? "))
            vehicle.add_fuel(fuel_to_add)
            print("Added {} units of fuel.\n".format(fuel_to_add))
        except TypeError:
            print("Invalid choice\n")
    else:
        print("Invalid choice\n")
    print("{}, fuel={}, odo={}".format(vehicle.name, vehicle.fuel, vehicle.odometer))
    print("Menu\nd) drive\nr) refuel\nq) quit")
    user_choice = str(input("Enter your choice: ")).lower()
print("Goodbye, {}'s driver.".format(vehicle.name))