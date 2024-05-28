import os

import helper
import web_handler as wh
# ideas
# gives suggestion for which car the user means if it's not in the list of cars
# 

def setup():
    """Setup the application, fetching necesary data."""
    wh.fetch_mpg()
    wh.fetch_maintenance()

def load_file(file):
    """Loads the content of a file and returns it as a string."""
    file_path = os.path.realpath(file)
    with open(file_path, 'r') as file:
        return file.read()
    
def print_menu(menu_items):
    """Prints the appropriate menu depending on users configurations."""
    if all(menu_items):
        print(load_file("final_project/output_files/menu_user_car12.txt"))
    elif menu_items[0] and menu_items[1]:
        print(load_file("final_project/output_files/menu_car12.txt"))
    elif menu_items[0] and menu_items[2]:
        print(load_file("final_project/output_files/menu_user_car1.txt"))
    elif menu_items[1] and menu_items[2]:
        print(load_file("final_project/output_files/menu_user_car2.txt"))
    elif menu_items[0]:
        print(load_file("final_project/output_files/menu_car1.txt"))
    elif menu_items[1]:
        print(load_file("final_project/output_files/menu_car2.txt"))
    elif menu_items[2]:
        print(load_file("final_project/output_files/menu_user.txt"))
    else:
        print(load_file("final_project/output_files/menu.txt"))

def main():
    """The main function of the application."""
    setup()
    os.system('cls||clear')
    print(load_file('final_project/output_files/car_loan_logo.txt'))

    valid_actions = '123456'
    menu_items = [False, False, False]
    while True:
        print_menu(menu_items)
        
        action = input("Choose Action: ")
        if action not in valid_actions:
            print("\n===    Invalid Action   ===\n")
            continue

        print('')
        match action:
            case '1' : print(load_file("final_project/output_files/information.txt"))
            case '2' : menu_items[0] = helper.configure_car(1)
            case '3' : menu_items[1] = helper.configure_car(2)
            case '4' : menu_items[2] = helper.configure_user()
            case '5' : helper.give_recommendation(menu_items)
            case '6' : break
    
    print(load_file('final_project/output_files/exit_program.txt'))

if __name__ == '__main__':
    main()