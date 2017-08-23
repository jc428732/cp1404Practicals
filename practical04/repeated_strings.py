strings_entered = set()
strings_repeated = []
user_input = str(input("Enter a string: "))

while user_input != "":
    if user_input in strings_entered and user_input not in strings_repeated:
        strings_repeated.append(user_input)
    else:
        strings_entered.add(user_input)
    user_input = str(input("Enter a string: "))

if strings_repeated == []:
    print("No repeated strings entered.")
else:
    print("Strings repeated: ", end="")
    for string in strings_repeated:
        print("{} ".format(string), end="")