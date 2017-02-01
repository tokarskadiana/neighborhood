from model.community import Community


class UrbanCommune(Community):
    __type_number = 1

    @classmethod
    def get_type_number(cls):
        return cls.__type_number
