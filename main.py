import os
import sys
from read_data import Data
from menu import Menu


def main():
    malopolska = Data('malopolska.csv').create_data()
    menu = Menu()
    while True:
        os.system('clear')
        print(menu.options())
        option = input('\nChose the option:')
        if option == '1':
            menu.list_statistics()
        elif option == '2':
            menu.print_longest_names()
        elif option == '3':
            menu.print_largest_county()
        elif option == '4':
            menu.print_multicategory_names()
        elif option == '5':
            menu.advanced_search()
        elif option == '0':
            sys.exit()


if __name__ == '__main__':
    main()
