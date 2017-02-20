from model.community import Community
from model.town import Town
from model.rural_area import RuralArea


class UrbanRuralCommune(Community):
    __type_number = 3

    def __init__(self, name, id, county_id, province_id):
        super().__init__(name, id, county_id, province_id)
        self.__town = self.set_town()
        self.__rural_area = self.set_rural_area()

    def set_town(self):
        for town in Town.get_list():
            if town.get_commune_id() == self.get_id() and town.get_province_id() == self.get_province_id():
                return town

    def set_rural_area(self):
        for rural_area in RuralArea.get_list():
            if rural_area.get_commune_id() == self.get_id() and rural_area.get_province_id() == self.get_province_id():
                return rural_area

    def get_town(self):
        return self.__town

    def get_rural_area(self):
        return self.__rural_area

    @classmethod
    def get_type_number(cls):
        return cls.__type_number
