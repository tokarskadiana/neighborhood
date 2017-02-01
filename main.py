import os
import sys
from read_data import Data
from model.district import District
from model.county import County
from model.community import Community

def main():
    menu = '''
    --------MENU--------
    (1) List statistics
    (2) Display 3 cities with longest names
    (3) Display county's name with the largest number of communities
    (4) Display locations, that belong to more than one category
    (5) Advanced search
    (0) Exit program
    '''

    malopolska = Data('malopolska.csv').create_data()
    while True:
        os.system('clear')
        print(menu)
        option = input('\nChose the option:')
        if option == '1':
            print(District.get_districts_list())
        elif option == '2':
            print(County.get_counties_list())
        elif option == '3':
            print(Community.get_communities_list())
        elif option == '4':
            pass
        elif option == '5':
            pass
        elif option == '0':
            sys.exit()


if __name__ == '__main__':
    main()
