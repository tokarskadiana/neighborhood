from model.unit import Unit
from model.county import County


class Province(Unit):
    __provinces_list = []

    def __init__(self, name, id):
        super().__init__(name, id)
        self.counties = self.set_counties()

    def set_counties(self):
        counties = []
        for county in County.get_counties_list():
            if county.get_province_id() == self.id:
                counties.append(county)
        return counties

    def get_counties(self):
        return self.counties

    @classmethod
    def create(cls, name, id):
        cls.__provinces_list.append(cls(name, id))

    @classmethod
    def get_provinces_list(cls):
        return cls.__provinces_list

    @classmethod
    def find_by_id(cls, province_id):
        for province in cls.__provinces_list:
            if province.id == province_id:
                return province
