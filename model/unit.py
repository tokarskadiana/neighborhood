class Unit:

    def __init__(self, name, id):
        self.name = name
        self.__id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.__id
