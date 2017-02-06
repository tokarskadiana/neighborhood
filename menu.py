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

    def to_pl(self):
        to_pl = {Province: 'wojewódstwo',
                 County: 'powiat',
                 City: 'miasto na prawach powiatu',
                 RuralCommune: 'gmina wiejska',
                 UrbanCommune: 'gmina miejska',
                 UrbanRuralCommune: 'gmina miejsko-wiejska',
                 RuralArea: 'obszar wiejski',
                 Town: 'miasto',
                 Delegacy: 'delegatura'}
        return to_pl

    def print_provinces(self):
        print('Chose the province to operate on:\n')
        for province in Province.get_provinces_list():
            print('[{}] {}'.format(province.get_id(), province.get_name()))

    def view_details(self, province_id):
        province = Province.find_by_id(province_id)
        if province:
            to_pl = self.to_pl()
            name = province.get_name()
            counties = province.get_counties()
            cities = 0
            delegacies = 0
            urban_comumnes = 0
            rural_communes = 0
            urban_rural_communes = 0
            towns = 0
            rural_areas = 0
            for county in counties:
                if type(county) == City:
                    cities += 1
                    delegacies += len(county.get_delegacies())
                for community in county.get_communities():
                    if type(community) == UrbanCommune:
                        urban_comumnes += 1
                    elif type(community) == RuralCommune:
                        rural_communes += 1
                    elif type(community) == UrbanRuralCommune:
                        urban_rural_communes += 1
                        towns += 1
                        rural_areas += 1

            data = [[Province, 1],
                    [County, len(counties)],
                    [UrbanCommune, urban_comumnes],
                    [RuralCommune, rural_communes],
                    [UrbanRuralCommune, urban_rural_communes],
                    [RuralArea, rural_areas],
                    [Town, towns],
                    [City, cities],
                    [Delegacy, delegacies]]
            for item in data:
                for key, value in to_pl.items():
                    if item[0] == key:
                        item[0] = value
            return name, tabulate(data, tablefmt="simple")
        return None

    def list_statistics(self):
        while True:
            os.system('clear')
            self.print_provinces()
            chose = input('\nEnter a province ID(x - to back):')
            if chose.lower() == 'x':
                break
            try:
                chose = int(chose)
                statistics = self.view_details(chose)
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
        towns = Town.get_towns_list()
        for county in County.get_counties_list():
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
        province = Province.find_by_id(province_id)
        if province:
            names = province.get_counties()
            for county in province.get_counties():
                names = names + county.get_communities()
                if type(county) == City:
                    names = names + county.get_delegacies()
                for community in county.get_communities():
                    if type(community) == UrbanRuralCommune:
                        names = names + [community.get_town()]
                        names = names + [community.get_rural_area()]
            names = list(map(lambda item: item.get_name(), names))
            return list(set((Counter(names[:]) - Counter(set(names[:]))).elements()))

    def columns(self, skills_defs, cols=2):
        pairs = ["\t".join(skills_defs[i:i + cols])
                 for i in range(0, len(skills_defs), cols)]
        return "\n".join(pairs)

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
                    print(self.make_columns(names, 4))
                    input('\nEnter something to back:')
            except ValueError:
                continue

    def advanced_search(self):  # search in all lists
        os.system('clear')
        data = Province.get_provinces_list() + County.get_counties_list() + Community.get_communities_list() + \
            Town.get_towns_list() + RuralArea.get_rural_areas_list() + \
            Delegacy.get_delegacies_list()
        search = input('Enter word or a part to start search:')
        temp_data = []
        for item in data:
            if search.lower() in item.get_name().lower():
                for key, value in self.to_pl().items():
                    if type(item) == key:
                        temp_data.append([item.get_name(), value])
        if temp_data:
            print(tabulate(sorted(temp_data, key=lambda x: (x[0], x[1])), tablefmt="simple"))
        else:
            print('There no matches. Search wasnt succesfull.')
        input('\nEnter something to back:')
