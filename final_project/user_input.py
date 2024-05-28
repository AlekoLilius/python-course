import re
import os
import json

def is_float(string):
    """Checks if string is a float"""
    try:
        float(string)
        return True
    except ValueError:
        return False

def get_vehicle_details():
    """Gets user input for vehicle details"""
    make, model, year, mileage, fuel_efficiency = '', '', '', 0, -1
    
    # Get make
    while True:
        make = input("Enter make (ex. Toyota, Audi, Nissan): ")
        if re.match(r"^[A-Z][a-z]+$", make.strip()):
            break
        print("\nWrong format! Needs to be a car brand\n")

    # Get model
    while True:
        model = input("Enter model (ex. Toyota Crown, Audi A6, Nissan Altima): ")
        if re.match(r"^(?:[A-Za-z0-9]+(?:[-\s]?[A-Za-z0-9]+)*)$", model):
            break
        print("\nWrong format! Needs to be a valid car model\n")

    # Get year
    while True:
        year = input("Enter year (ex. 1950, 2005, 2024): ")
        if year.strip().isdigit() and 1950 <= int(year) <= 2024:
            break
        print("\nWrong format! Needs to be YYYY within 1950-2024.\n")
    
    # Get mileage
    while True:
        mileage_input = input("Enter mileage in km (ex. 0, 1000, 20000): ")
        if mileage_input.strip().isdigit() and 0 <= int(mileage_input) <= 50000:
            mileage = int(mileage_input)
            break
        print("\nWrong format! Needs to be number within 0-50000.\n")

    # Load mpg data
    with open(os.path.realpath('final_project/web_files/cars_mpg.json'), 'r') as f:
        cars_mpg = json.load(f)
    # Check if car model is in list of cars
    for car in cars_mpg:
        if model.lower() in car:
            fuel_efficiency = cars_mpg[car]
            break
    # If fuel efficiency not found, prompt user to enter fuel efficiency
    if fuel_efficiency == -1:
        while True:
            fuel_efficiency = input("Enter fuel efficiency in mpg (ex. 20.1, 30.5, 40): ")
            if is_float(fuel_efficiency.strip()) and 0 <= float(fuel_efficiency) <= 500:
                fuel_efficiency = float(fuel_efficiency)
                break
            print("\nWrong format! Needs to be number within 0-50000.\n")

    return make, model, year, mileage, fuel_efficiency

def get_maintenance(model):
    """Gets maintenance costs if it exists, otherwise get it from user input"""
    maintenance = -1
    # Load maintenance data
    with open(os.path.realpath('final_project/web_files/cars_maintenance.json'), 'r') as f:
        cars_maintenance = json.load(f)
    # Check if car model is in list of cars
    for car in cars_maintenance:
        if model.lower() in car:
            maintenance = cars_maintenance[car]
            break
    # If car maintenance not found, prompt user to enter car maintenance
    if maintenance == -1:
        while True:
            maintenance = input("Enter annual maintenance cost in € (ex. 5000, 10000, 15000): ")
            if maintenance.strip().isdigit() and 0 <= int(maintenance) <= 50000:
                maintenance = int(maintenance)
                break
            print("\nWrong format! Needs to be number within 0-50000.\n")

    return maintenance


def get_expected_price():
    """Gets user input for expected price of a car"""
    while True:
        expected_price = input("Enter expected price for the car in € (ex. 5000, 10000, 20000): ")
        if expected_price.strip().isdigit() and 100 <= int(expected_price) <= 1000000:
            return int(expected_price)
        print("\nWrong format! Needs to be a number within 100-1000000.\n")

def get_driving_habits():
    """Gets user input for driving habits"""
    res = []
    weekday_mileage, weekend_mileage = 0, 0
    while True:
        weekday_mileage = input("Enter weekday mileage in km (ex. 0, 10, 50): ")
        if weekday_mileage.strip().isdigit() and 0 <= int(weekday_mileage) <= 1000:
            res.append(int(weekday_mileage))
            break
        else:
            print("\nWrong format! Needs to be a number within 0-1000.\n")
    while True:
        weekend_mileage = input("Enter weekend mileage in km (ex. 0, 10, 50): ")
        if weekend_mileage.strip().isdigit() and 0 <= int(weekend_mileage) <= 1000:
            res.append(int(weekend_mileage))
            break
        else:
            print("\nWrong format! Needs to be a number within 0-1000.\n")
    return res

def get_interest_rate():
    """Gets user input for interest rate of the loan"""
    while True:
        interest_rate = input("Enter interest rate for the loan in % (ex. 0, 2.5, 5): ")
        if is_float(interest_rate.strip()) and 0 <= float(interest_rate) <= 100:
            return float(interest_rate) / 100 # convert to percentage interest rate
        print("\nWrong format! Needs to be a number within 0-100.\n")

def get_down_payment():
    """Gets user input for down payment"""
    while True:
        down_payment = input("Do you want to add down payment? (y/n): ")
        if down_payment.strip().lower() == 'y':
            while True:
                dp_value = input("Enter down payment value in € (ex. 1000, 5000, 10000): ")
                if dp_value.strip().isdigit() and 1 <= int(dp_value) <= 100000:
                    return int(dp_value)
                print("\nWrong format! Needs to be a number within 1-100000.\n")
        if down_payment.strip().lower() == 'n':
            print("No down payment added.")
            return 0
        else:
            print("\nWorng format! Needs to be 'y' or 'n'.\n")

def lookup_car():
    pass