x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))

user_selection = int(input("Select an option:\n1: Show the even numbers from x to y.\n2: Show the odd numbers from x to y.\n3: Show the squares from x to y.\n4: Exit the program.\n"))

if user_selection == 1:
    if x % 2 == 0:
        for i in range(x, y + 1, 2):
            print(i, end=' ')
        print()
    else:
        for i in range(x - 1, y + 1, 2):
            print(i, end=' ')
        print()
elif user_selection == 2:
    if x % 2 == 1:
        for i in range(x, y + 1, 2):
            print(i, end=' ')
        print()
    else:
        for i in range(x + 1, y + 1, 2):
            print(i, end=' ')
        print()
elif user_selection == 3:
    for i in range(x, y):
        rounded_square_root = int(round(i ** 0.5))
        if rounded_square_root ** 2 == i:
            print(i, end=' ')
    print()
elif user_selection != 4:
    print("Invalid input.\n")
print("Program exited.")