class Town:
    __type_number = 4
    __towns_list = []

    def __init__(self, name, commune_id, province_id):
        self.__name = name
        self.__commune_id = commune_id
        self.__province_id = province_id

    def get_commune_id(self):
        return self.__commune_id

    def get_name(self):
        return self.__name

    def get_province_id(self):
        return self.__province_id

    @classmethod
    def get_type_number(cls):
        return cls.__type_number

    @classmethod
    def create(cls, name, commune_id, province_id):
        cls.__towns_list.append(cls(name, commune_id, province_id))

    @classmethod
    def get_towns_list(cls):
        return cls.__towns_list
