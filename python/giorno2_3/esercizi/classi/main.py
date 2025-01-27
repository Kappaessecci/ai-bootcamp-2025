class Country:
    def __init__(self, name):
        self.name = name
        self.regions = []

    def add(self, region):
        self.regions.append(region)

    @property
    def pop(self):
        return sum(region.pop for region in self.regions)

    @property
    def most_populuous_city(self):
        cities = [city for region in self.regions for city in region.cities]
        if cities:
            return max(cities, key=lambda city: city.pop)

class Region:
    def __init__(self, name):
        self.name = name
        self.cities = []

    def add(self, city):
        self.cities.append(city)

    @property
    def pop(self):
        return sum(city.pop for city in self.cities)

class City:
    def __init__(self, name, pop=None):
        self.name = name
        self.pop = pop