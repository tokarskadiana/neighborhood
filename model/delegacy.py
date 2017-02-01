class Delegacy:
    __type_number = 9
    __delegacies_list = []

    def __init__(self, name, city_id):
        self.name = name
        self.city_id = city_id

    @classmethod
    def get_type_number(cls):
        return cls.__type_number

    @classmethod
    def create(cls, name, city_id):
        cls.__delegacies_list.append(cls(name, city_id))

    @classmethod
    def get_delegacies_list(cls):
        return cls.__delegacies_list
