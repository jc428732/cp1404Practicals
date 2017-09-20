from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035)
another_guitar = Guitar("Another Guitar", 2012, 15)
print("{} {} - Expected {}. Got {}".format(gibson.name, "get _age()", 95, gibson.get_age()))
print("{} {} - Expected {}. Got {}".format(gibson.name, "is_vintage()", True, gibson.is_vintage()))
print("{} {} - Expected {}. Got {}".format(another_guitar.name, "get _age()", 5, another_guitar.get_age()))
print("{} {} - Expected {}. Got {}".format(another_guitar.name, "is_vintage()", False, another_guitar.is_vintage()))
