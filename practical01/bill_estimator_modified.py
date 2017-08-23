print("Electricity bill estimator.")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
current_tariff = int(input("Which tariff? 11 or 31: "))
if current_tariff == 11:
    cents_per_kWh = TARIFF_11 * 100
elif current_tariff == 31:
    cents_per_kWh = TARIFF_31 * 100
else:
    print("Tariff not recognised.")
    cents_per_kWh = float(input("Enter cents per kWh: "))
daily_use_kWh = float(input("Enter daily use in kWh: "))
number_of_billing_days = float(input("Enter number of billing days: "))
estimated_bill = cents_per_kWh * 0.01 * daily_use_kWh * number_of_billing_days

print("Estimated bill: ${:.2f}".format(estimated_bill))