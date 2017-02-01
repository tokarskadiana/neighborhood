class RuralArea:
    __type_number = 5
    __rural_areas_list = []

    def __init__(self, name, commune_id):
        self.__name = name
        self.__commune_id = commune_id

    def get_commune_id(self):
        return self.__commune_id

    @classmethod
    def get_type_number(cls):
        return cls.__type_number

    @classmethod
    def create(cls, name, commune_id):
        cls.__rural_areas_list.append(cls(name, commune_id))

    @classmethod
    def get_rural_areas_list(cls):
        return cls.__rural_areas_list
