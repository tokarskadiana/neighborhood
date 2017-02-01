from model.unit import Unit
from model.county import County


class District(Unit):
    __districts_list = []

    def __init__(self, name, id):
        super().__init__(name, id)
        self.counties = self.set_counties()

    def set_counties(self):
        counties = []
        for county in County.get_counties_list():
            if county.get_district_id = self.id:
                counties.append.(county)
        return counties

    @classmethod
    def create(cls, name, id):
        cls.__districts_list.append(cls(name, id))

    @classmethod
    def get_districts_list(cls):
        return cls.__districts_list
