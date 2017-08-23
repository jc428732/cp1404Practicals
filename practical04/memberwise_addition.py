def memberwise_addition(list1, list2):
    if len(list1) >= len(list2):
        larger_list = list1
        smaller_list = list2
    else:
        larger_list = list2
        smaller_list = list1
    x = 0
    output_list = []
    for number in larger_list:
        try:
            output_list.append(number + smaller_list[x])
        except IndexError:
            output_list.append(number)
        x += 1
    return output_list

lista = [1, 2, 3, 4, 5]
listb = [1, 2, 3]
print(memberwise_addition(lista, listb))