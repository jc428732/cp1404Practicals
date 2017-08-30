def lists_to_dictionary(list1, list2):
    dictionary = {}
    x = 0
    for item in list1:
        dictionary[item] = list2[x]
        x += 1
    return dictionary

# dictionary_of_people = lists_to_dictionary( ["Jack", "Jill", "Harry"], [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)])
# print(dictionary_of_people)