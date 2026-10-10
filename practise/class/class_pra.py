class Country():
    def __init__(self, name):
        self.name = name
        self.population = None

    def add_population(self, population):
        self.population = population

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_population(self):
        return self.population