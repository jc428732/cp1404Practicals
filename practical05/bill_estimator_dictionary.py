print("Electricity Bill Estimator 2.0")
tariffs = {"TARIFF_11": 0.244618, "TARIFF_31": 0.136928, "TARIFF_1000000000": 0.18, "TARIFF_14": 0.05, "TARIFF_33": 0.2}
current_tariff = str(input("Which tariff? "))
if "TARIFF_" + current_tariff in tariffs:
    cents_per_kWh = tariffs["TARIFF_" + current_tariff] * 100
else:
    print("Tariff not recognised.")
    cents_per_kWh = float(input("Enter cents per kWh: "))
daily_use_kWh = float(input("Enter daily use in kWh: "))
number_of_billing_days = float(input("Enter number of billing days: "))
estimated_bill = cents_per_kWh * 0.01 * daily_use_kWh * number_of_billing_days

print("Estimated bill: ${:.2f}".format(estimated_bill))
