from model.unit import Unit
from model.community import Community


class County(Unit):
    __counties_list = []

    def __init__(self, name, id, district_id):
        super().__init__(name, id)
        self.district_id = district_id
        self.communities = self.set_communities()

    def set_communities(self):
        communities = []
        for community in Community.get_communities_list():
            if community.get_county_id = self.id:
                communities.append(community)
        return communities

    def get_district_id(self):
        return self.district_id

    @classmethod
    def create(cls, name, id, district_id):
        cls.__counties_list.appent(cls(name, id, district_id))

    @classmethod
    def get_counties_list(cls):
        return cls.__counties_list
