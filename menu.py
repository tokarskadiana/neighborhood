import os
from collections import Counter
from tabulate import tabulate
from read_data import Data
from model.province import Province
from model.county import County
from model.city import City
from model.community import Community
from model.rural_commune import RuralCommune
from model.urban_commune import UrbanCommune
from model.urban_rural_commune import UrbanRuralCommune
from model.delegacy import Delegacy
from model.rural_area import RuralArea
from model.town import Town


class Menu:

    def options(self):
        menu = '''
        --------MENU--------
        (1) List statistics
        (2) Display 3 cities with longest names
        (3) Display county's name with the largest number of communities
        (4) Display locations, that belong to more than one category
        (5) Advanced search
        (0) Exit program
        '''
        return menu

    def units(self):
        units = {Province: 'wojewódstwo',
                 County: 'powiat',
                 City: 'miasto na prawach powiatu',
                 RuralCommune: 'gmina wiejska',
                 UrbanCommune: 'gmina miejska',
                 UrbanRuralCommune: 'gmina miejsko-wiejska',
                 RuralArea: 'obszar wiejski',
                 Town: 'miasto',
                 Delegacy: 'delegatura'}
        return units

    def print_provinces(self):
        print('Chose the province to operate on:\n')
        for province in Province.get_list():
            print('[{}] {}'.format(province.get_id(), province.get_name()))

    def all_units_list(self):
        data = County.get_list() + Community.get_list() + Town.get_list() + \
            RuralArea.get_list() + Delegacy.get_list()
        return data

    def make_columns(self, list_to, cols):
        list_done = []
        n = len(list_to)
        i = 0
        while True:
            if i + cols >= n:
                list_done.append(list_to[i:])
                break
            else:
                list_done.append(list_to[i:i + cols])
                i += cols
        return tabulate(list_done, tablefmt='simple')

    def get_statistics(self, province_id):
        province = Province.find_by_id(province_id)
        if province:
            units = self.units()
            name = province.get_name()
            counties = province.get_counties()
            cities, delegacies, urban_communes, rural_communes, urban_rural_communes, towns, rural_areas = (0,)*7
            for county in counties:
                if type(county) == City:
                    cities += 1
                    delegacies += len(county.get_delegacies())
                for community in county.get_communities():
                    if type(community) == UrbanCommune:
                        urban_communes += 1
                    elif type(community) == RuralCommune:
                        rural_communes += 1
                    elif type(community) == UrbanRuralCommune:
                        urban_rural_communes += 1
                        towns += 1
                        rural_areas += 1
            data = [[Province, 1],
                    [County, len(counties)],
                    [UrbanCommune, urban_communes],
                    [RuralCommune, rural_communes],
                    [UrbanRuralCommune, urban_rural_communes],
                    [RuralArea, rural_areas],
                    [Town, towns],
                    [City, cities],
                    [Delegacy, delegacies]]
            for item in data:
                for key, value in units.items():
                    if item[0] == key:
                        item[0] = value
            return name, tabulate(data, tablefmt="simple")
        return None

    def print_statistics(self):
        while True:
            os.system('clear')
            self.print_provinces()
            chose = input('\nEnter a province ID(x - to back):')
            if chose.lower() == 'x':
                break
            try:
                chose = int(chose)
                statistics = self.get_statistics(chose)
                if statistics:
                    os.system('clear')
                    print(statistics[0])
                    print(statistics[1])
                    input('\nEnter something to back:')
                else:
                    continue
            except ValueError:
                continue

    def find_longest_names(self):
        towns = Town.get_list()
        for county in County.get_list():
            if type(county) == City:
                towns.append(county)
        towns = map(lambda town: town.get_name(), towns)
        data = sorted(towns, key=len)[-3:]
        return data[::-1]

    def print_longest_names(self):
        os.system('clear')
        data = self.find_longest_names()
        for index, item in enumerate(data):
            print('{}. {}'.format(index + 1, item))
        input('\nEnter something to back:')

    def get_largest_county(self, distrist_id):
        province = Province.find_by_id(distrist_id)
        if province:
            counties = province.get_counties()
            county = max(counties, key=lambda county: len(
                county.get_communities()))
            return province.get_name(), county.get_name(), len(county.get_communities())

    def print_largest_county(self):
        while True:
            os.system('clear')
            self.print_provinces()
            chose = input('\nEnter a province ID(x - to back):')
            if chose.lower() == 'x':
                break
            try:
                chose = int(chose)
                county_info = self.get_largest_county(chose)
                if county_info:
                    os.system('clear')
                    print('''
        In {} province the county with largest number of communities is: {}.
        It has {} communities.'''.format(county_info[0], county_info[1], county_info[2]))
                    input('\nEnter something to back:')
            except ValueError:
                continue

    def find_multicategory_names(self, province_id):
        data = self.all_units_list()
        locations = []
        for item in data:
            if item.get_province_id() == province_id:
                locations.append(item.get_name())
        counter = Counter(locations)
        print(counter)
        for name, count in counter.items():
            if count <= 1:
                locations.remove(name)
        return list(set(locations))

    def print_multicategory_names(self):
        while True:
            os.system('clear')
            self.print_provinces()
            chose = input('\nEnter a province ID(x - to back):')
            if chose.lower() == 'x':
                break
            try:
                chose = int(chose)
                names = self.find_multicategory_names(chose)
                if names:
                    os.system('clear')
                    print(self.make_columns(sorted(names), 4))
                    input('\nEnter something to back:')
            except ValueError:
                continue

    def advanced_search(self):  # search in all lists
        os.system('clear')
        data = Province.get_list() + self.all_units_list()
        search = input('Enter word or a part to start search:')
        temp_data = []
        for item in data:
            if search.lower() in item.get_name().lower():
                for key, value in self.units().items():
                    if type(item) == key:
                        temp_data.append([item.get_name(), value])
        if temp_data:
            print(tabulate(sorted(temp_data, key=lambda x: (x[0], x[1])), tablefmt="simple"))
        else:
            print('There no matches. Search wasnt succesfull.')
        input('\nEnter something to back:')
