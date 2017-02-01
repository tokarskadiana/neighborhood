class Delegacy:
    __type_number = 9

    def __init__(self, name, city_id):
        self.name = name
        self.city_id = city_id

    def get_type_number(self):
        return self.__type_number
