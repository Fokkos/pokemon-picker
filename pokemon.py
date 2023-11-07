import math


class Pokemon:
    def __init__(self, dex, name, complexity, realism, artificiality, fantasy, humanoid, cuteness, coolness, beauty, popularity):
        self.dex = dex
        self.name = name
        self.complexity = complexity
        self.realism = realism
        self.artificiality = artificiality
        self.fantasy = fantasy
        self.humanoid = humanoid
        self.cuteness = cuteness
        self.coolness = coolness
        self.beauty = beauty
        self.popularity = popularity

    def __repr__(self):
        return repr(f"{self.name}'s dex number is {self.dex}")

    def is_valid(self):
        for data in (self.complexity, self.realism, self.artificiality, self.fantasy, self.humanoid, self.cuteness,
                    self.coolness, self.beauty, self.popularity):
            if math.isnan(data):
                return False
        return True

