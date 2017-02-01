from model.community import community
from model.town import Town
from model.rural_area import RuralArea


class UrbanRuralCommune(Community):
    __type_number = 3

    def __init__(self, name, id, county_id):
        super().__init__(name, id, county_id)
        self.town = self.set_town()
        self.rural_area = self.set_rural_area()

    def set_town(self):
        for town in Town.get_towns_list():
            if town.get_commune_id == self.id:
                return town

    def set_rural_area(self):
        for rural_area in RuralArea.get_rural_areas_list():
            if rural_area.get_commune_id == self.id:
                return rural_area
