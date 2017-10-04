from practical08.taxi import Taxi
from practical08.silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
print("Let's drive!")
user_input = " "
total_fare = 0
current_taxi = False
total_distance = 0
while user_input != "q":
    user_input = input("q)uit, c)hoose taxi, d)rive\n")
    if user_input == "c":
        index = 0
        print("Taxis available:")
        for taxi in taxis:
            print("{} - {}".format(index, taxi))
            index += 1
        current_taxi = taxis[int(input("Choose taxi: "))]
        print("Bill to date: ${:.2f}".format(total_fare))
        current_taxi.start_fare()
    elif (user_input == "d") & current_taxi:
        total_distance += current_taxi.drive(int(input("Drive how far? ")))
        total_fare += current_taxi.get_fare()
        print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
        print("Bill to date: ${:.2f}".format(total_fare))
print("Total trip cost: ${:.2f}".format(total_fare))
index = 0
print("Taxis are now:")
for taxi in taxis:
    print("{} - {}".format(index, taxi))
    index += 1