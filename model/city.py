from model.county import County
from model.delegacy import Delegacy


class City(County):
    '''
    Represents city with county rights object
    '''
    __cities_list = []

    def __init__(self, name, id, district_id):
        super().__init__(name, id, district_id)
        self.communities = self.set_communities()
        self.delegacies = self.set_delegacies()

    def set_delegacies(self):
        delegacies = []
        for delegacy in Delegacy.get_delegacies_list():
            if delegacy.get_city_id == self.id:
                delegacies.append(delegacy)
        return delegacies

    @classmethod
    def get_cities_list(cls):
        return cls.__cities_list
