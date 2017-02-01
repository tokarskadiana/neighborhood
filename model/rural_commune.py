from model.community import Community


class RuralCommune(Community):
    __type_number = 2

    @classmethod
    def get_type_number(cls):
        return cls.__type_number
