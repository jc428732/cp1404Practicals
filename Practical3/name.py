def main():
    name = str(input("What is your name?\n"))
    get_name(name)


def get_name(name, frequency):
    if len(name) > 0:
        for letter in range(0, len(name)):
            if letter % frequency:
                print(name[letter])


main()