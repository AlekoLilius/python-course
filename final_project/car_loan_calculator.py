import os

# ideas
# gives suggestion for which car the user means if it's not in the list of cars
# 

def load_file(file):
    """Loads the content of a file and returns it as a string."""
    file_path = os.path.realpath(file)
    with open(file_path, 'r') as file:
        return file.read()

def main():
    print(load_file('final_project/output_files/car_loan_logo.txt'))

    valid_actions = '12345'
    while True:
        print(load_file("final_project/output_files/menu.txt"))
        
        action = input("Choose Action: ")
        if action not in valid_actions:
            print("\n===    Invalid Action   ===\n")
            continue

        match action:
            case '1' : print(load_file("final_project/output_files/information.txt"))
            case '2' : pass
            case '3' : pass
            case '4' : pass
            case '5' : break

if __name__ == '__main__':
    main()