def main():
    name = str(input("What is your name?\n"))
    get_name(name, 2)


def get_name(name, frequency):
    if len(name) > 0:
        for letter in range(frequency - 1, len(name), frequency):
            print(name[letter])


main()