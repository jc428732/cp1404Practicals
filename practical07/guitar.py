
class Guitar(object):

    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{:15} ({:4}) : ${:6}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2017 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        return False