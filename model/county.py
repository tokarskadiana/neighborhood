from model.unit import Unit
from model.community import Community


class County(Unit):
    __counties_list = []

    def __init__(self, name, id, province_id):
        super().__init__(name, id)
        self.province_id = province_id
        self.communities = self.set_communities()

    def set_communities(self):
        communities = []
        for community in Community.get_communities_list():
            if community.get_county_id() == self.id and community.get_province_id() == self.get_province_id():
                communities.append(community)
        return communities

    def get_province_id(self):
        return self.province_id

    def get_communities(self):
        return self.communities

    @classmethod
    def create(cls, name, id, province_id):
        cls.__counties_list.append(cls(name, id, province_id))

    @classmethod
    def get_counties_list(cls):
        return cls.__counties_list
