class Town:
    __type_number = 4

    def __init__(self, name, commune_id):
        self.name = name
        self.commune_id = commune_id

    def get_type_number(self):
        return self.__type_number
