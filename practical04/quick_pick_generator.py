import random

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(0, number_of_quick_picks):
    numbers = []
    while len(numbers) < 6:
        generated_number = random.randint(1, 45)
        if generated_number not in numbers:
            numbers.append(generated_number)
    numbers.sort()
    for number in numbers:
        print("{:3}".format(number),end="")
    print("")