import os
import sys
from read_data import Data
from model.district import District
from model.county import County
from model.community import Community
from model.rural_commune import RuralCommune
from model.rural_area import RuralArea
from model.town import Town
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
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == '5':
            pass
        elif option == '0':
            sys.exit()


if __name__ == '__main__':
    main()
