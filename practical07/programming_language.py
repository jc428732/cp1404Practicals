class ProgrammingLanguage(object):
    def __init__(self, name='', typing='Static', reflection=False, year=1900):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, str(self.reflection),
                                                                           str(self.year))

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        return False
