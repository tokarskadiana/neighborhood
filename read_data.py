import csv
from model.town import Town
from model.rural_area import RuralArea
from model.community import Community
from model.delegacy import Delegacy
from model.rural_commune import RuralCommune
from model.urban_commune import UrbanCommune
from model.urban_rural_commune import UrbanRuralCommune
from model.county import County
from model.city import City
from model.province import Province


class Data:

    def __init__(self, filename):
        self.filename = filename

    def convert(self, chars):
        try:
            chars = int(chars)
        except ValueError:
            pass
        return chars

    def open_csv(self):
        data = []
        with open(self.filename) as csv_file:
            for row in csv.reader(csv_file, delimiter='\t'):
                data.append([self.convert(char) for char in row])
        return data

    def create_towns(self):
        for row in self.open_csv():
            if row[3] == Town.get_type_number():
                Town.create(row[4], row[2], row[0])

    def create_rural_areas(self):
        for row in self.open_csv():
            if row[3] == RuralArea.get_type_number():
                RuralArea.create(row[4], row[2], row[0])

    def create_delegacies(self):
        for row in self.open_csv():
            if row[3] == Delegacy.get_type_number():
                Delegacy.create(row[4], row[2], row[1], row[0])

    def create_communities(self):
        for row in self.open_csv():
            if row[3] == RuralCommune.get_type_number():
                RuralCommune.create(row[4], row[2], row[1], row[0])
            if row[3] == UrbanCommune.get_type_number():
                UrbanCommune.create(row[4], row[2], row[1], row[0])
            if row[3] == UrbanRuralCommune.get_type_number():
                UrbanRuralCommune.create(row[4], row[2], row[1], row[0])

    def create_counties(self):
        for row in self.open_csv():
            if row[1]:
                if not row[2]:
                    if row[1] > 60:
                        City.create(row[4], row[1], row[0])
                    else:
                        County.create(row[4], row[1], row[0])

    def create_province(self):
        for row in self.open_csv():
            if not row[1]:
                Province.create(row[4], row[0])

    def create_data(self):
        print("Load data.......")
        self.create_towns()
        self.create_rural_areas()
        self.create_delegacies()
        self.create_communities()
        self.create_counties()
        self.create_province()
