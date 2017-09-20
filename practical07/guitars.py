
from practical07.guitar import Guitar

guitars = []
vintage_string = ""
guitar_name = input("Name: ")
while guitar_name != '':
    guitar_year = int(input("Year: "))
    guitar_cost = int(input("Cost: $"))
    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    guitar_name = input("Name: ")
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}:".format(i + 1), "{self.name:>20} ({self.year}), worth ${self.cost:10,.2f}".format(self=guitar),
          "{}".format(vintage_string))
