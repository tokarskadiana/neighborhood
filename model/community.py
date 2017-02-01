from model.unit import Unit


class Community(Unit):
    __type_number = None

    def __init__(self, name, id, county_id):
        super().__init__(name, id)
        self.county_id = county_id

    def get_type_number(self):
        return self.__type_number
