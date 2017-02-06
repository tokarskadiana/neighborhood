from model.unit import Unit


class Delegacy(Unit):
    __type_number = 9
    __delegacies_list = []

    def __init__(self, name, id, city_id):
        super().__init__(name, id)
        self.__city_id = city_id

    def get_city_id(self):
        return self.__city_id

    @classmethod
    def get_type_number(cls):
        return cls.__type_number

    @classmethod
    def create(cls, name, id, city_id):
        cls.__delegacies_list.append(cls(name, id, city_id))

    @classmethod
    def get_delegacies_list(cls):
        return cls.__delegacies_list
