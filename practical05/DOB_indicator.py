
number_of_people = int(input("Number of people: "))
dictionary_of_people = {}
for i in range (0, number_of_people):
    person = str(input("Enter a name: "))
    dictionary_of_people[person] = str(input("Enter a date of birth: ")).split("/")
for entry in dictionary_of_people:
    print("{} is {} years old.".format(entry, 2017 - int(dictionary_of_people[entry][2])))