from model.unit import Unit


class Community(Unit):
    __list = []

    def __init__(self, name, id, county_id, province_id):
        super().__init__(name, id)
        self.__county_id = county_id
        self.__province_id = province_id

    def get_county_id(self):
        return self.__county_id

    def get_province_id(self):
        return self.__province_id

    @classmethod
    def create(cls, name, id, county_id, province_id):
        cls.__list.append(cls(name, id, county_id, province_id))

    @classmethod
    def get_list(cls):
        return cls.__list
