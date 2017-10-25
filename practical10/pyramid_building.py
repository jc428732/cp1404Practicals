
def calculate_number_of_blocks(number_of_rows):
    # total = 0
    # for n in range (number_of_rows, 0, -1):
    #     total += n
    # return total
    if number_of_rows >= 1:
        return number_of_rows + calculate_number_of_blocks(number_of_rows - 1)
    return 0

print(calculate_number_of_blocks(6))