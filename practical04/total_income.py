"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month {}:".format(month)))
        incomes.append(income)

    print_report("Month", incomes)


def print_report(time_period_type, values):
    print("\nIncome Report\n-------------")
    total = 0
    for time_period in range(1, len(values) + 1):
        value = values[time_period - 1]
        total += value
        print("{} {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(time_period_type, time_period, value, total))


main()
