print("Electricity bill estimator.")
cents_per_kWh = float(input("Enter cents per kWh: "))
daily_use_kWh = float(input("Enter daily use in kWh: "))
number_of_billing_days = float(input("Enter number of billing days: "))
estimated_bill = cents_per_kWh * 0.01 * daily_use_kWh * number_of_billing_days

print("Estimated bill: ${:.2f}".format(estimated_bill))