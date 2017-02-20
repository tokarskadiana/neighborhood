from model.county import County
from model.delegacy import Delegacy


class City(County):
    '''
    Represents city with county rights object
    '''
    def __init__(self, name, id, district_id):
        super().__init__(name, id, district_id)
        self.communities = self.set_communities()
        self.delegacies = self.set_delegacies()

    def set_delegacies(self):
        delegacies = []
        for delegacy in Delegacy.get_list():
            if delegacy.get_city_id() == self.get_id() and delegacy.get_province_id() == self.get_province_id():
                delegacies.append(delegacy)
        return delegacies

    def get_delegacies(self):
        return self.delegacies
