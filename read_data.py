import csv
from model.town import Town
from model.rural_area import RuralArea
from model.delegacy import Delegacy
from model.rural_commune import RuralCommune
from model.urban_commune import UrbanCommune
from model.urban_rural_commune import UrbanRuralCommune
from model.county import County
from model.city import City
from model.district import District


class Data:

    def __init__(self, filename):
        self.filename = filename

    def convert(self, s):
        try:
            s = int(s)
        except ValueError:
            pass
        return s

    def open_csv(self):
        data = []
        with open(self.filename) as csv_file:
            for row in csv.reader(csv_file, delimiter='\t'):
                data.append([self.convert(s) for s in row])
        return data

    def create_towns(self):
        for row in self.open_csv():
            if row[3] == Town.get_type_number():
                Town.create(row[4], row[2])

    def create_rural_areas(self):
        for row in self.open_csv():
            if row[3] == RuralArea.get_type_number():
                RuralArea.create(row[4], row[2])

    def create_delegacies(self):
        for row in self.open_csv():
            if row[3] == Delegacy.get_type_number():
                Delegacy.create(row[4], row[2])

    def create_communities(self):
        for row in self.open_csv():
            if row[3] == RuralCommune.get_type_number():
                RuralCommune.create(row[4], row[2], row[1])
            if row[3] == UrbanCommune.get_type_number():
                UrbanCommune.create(row[4], row[2], row[1])
            if row[3] == UrbanRuralCommune.get_type_number():
                UrbanRuralCommune.create(row[4], row[2], row[1])

    def create_counties(self):
        for row in self.open_csv():
            if row[1]:
                if not row[2]:
                    if row[5] == 'powiat':
                        County.create(row[4], row[1], row[0])
                    else:
                        City.create(row[4], row[1], row[0])

    def create_district(self):
        for row in self.open_csv():
            if not row[1]:
                District.create(row[4], row[0])

    def create_data(self):
        self.create_towns()
        self.create_rural_areas()
        self.create_delegacies()
        self.create_communities()
        self.create_counties()
        self.create_district()
