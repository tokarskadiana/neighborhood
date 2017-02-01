from model.unit import Unit


class County(Unit):
    def __init__(self, name, id, district_id):
        super().__init__(name, id)
        self.district_id = district_id
        self.communities = []
