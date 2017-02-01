from model.community import community


class UrbanRuralCommune(Community):
    __type_number = 3

    def __init__(self, name, id, county_id):
        super().__init__(name, id, county_id)
        self.town = None
        self.rural_area = None
