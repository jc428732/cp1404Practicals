from silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Taxi", 100, 2)
taxi.drive(18)
print(taxi, taxi.get_fare())