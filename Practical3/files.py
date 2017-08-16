out_file = open('name.txt', 'w')
name = str(input("What is your name?\n"))
print(name, file = out_file)
out_file.close()

in_file = open('name.txt', 'r')
name = in_file.read()
print("Your name is {}".format(name))
in_file.close()

in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    number = int(line.strip())
    total += number
print(total)
in_file.close()