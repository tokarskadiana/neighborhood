from model.unit import Unit


class District(Unit):

    def __init__(self, name, id):
        super().__init__(name, id)
        self.counties = []
