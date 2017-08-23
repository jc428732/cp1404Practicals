numbers = []
input_size = 5
for i in range(0, input_size):
    numbers.append(int(input("Number: ")))
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers) / input_size))