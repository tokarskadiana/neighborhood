from model.county import county


class City(County):
    '''
    Represents city with county rights object
    '''
    def __init__(self, name, id, district_id):
        super().__init__(name, id, district_id)
        self.counties = []
        self.delegacies = []
