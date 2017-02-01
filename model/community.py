from model.unit import Unit


class Community(Unit):
    __communities_list = []

    def __init__(self, name, id, county_id):
        super().__init__(name, id)
        self.county_id = county_id

    def get_county_id(self):
        return self.county_id

    @classmethod
    def create(cls, name, id, county_id):
        cls.__communities_list.append(cls(name, id, county_id))

    @classmethod
    def get_communities_list(cls):
        return cls.__communities_list
