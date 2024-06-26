import user_input as uinput
import user_information as uinfo
import car
import web_handler

# Initializing data variables
cars = {}
user_info = None

def configure_car(car_nbr):
    """
    
    Configures a car based on user input and car number.
    
    Parameters:
        car_nbr (int): The car number to configure.
    
    Returns:
        bool: True when car information is configured.

    """
    make, model, year, mileage, fuel_efficiency = uinput.get_vehicle_details()
    expected_price = uinput.get_expected_price()
    maintenance = uinput.get_maintenance(model)

    vehicle = car.Car(car_nbr, make, model, year, mileage, fuel_efficiency, expected_price, maintenance)
    cars[car_nbr] = vehicle
    return True

def configure_user():
    """
    
    Configures user based on user input.

    Returns:
        bool: True when user information is configured.
    
    """
    global user_info # Needed to update user_info

    driving_habits = uinput.get_driving_habits()
    interest_rate = uinput.get_interest_rate()
    down_payment = uinput.get_down_payment()

    # Create new user if none existed before or update existing user
    if user_info is None:
        user_info = uinfo.UserInformation(driving_habits, interest_rate, down_payment)
    else:
        user_info.update_info(driving_habits, interest_rate, down_payment)

    # Set cars depending on the provided cars
    if 1 in cars and 2 in cars:
        user_info.set_car(1, cars[1])
        user_info.set_car(2, cars[2])
    elif 1 in cars:
        user_info.set_car(1, cars[1])
    elif 2 in cars:
        user_info.set_car(2, cars[2])
    
    return True


def calculate_gas_cost(car, user_information):
    """
    
    Calculates gas cost for provided car number.
    
    Parameters:
        car (car): The car to use for gas cost calculation.

    Returns:
        float: Gas cost for provided car number.

    """
    return (car.fuel_efficiency * sum(user_information.driving_habits)) / 12

def calculate_maintenance(car):
    """
    Calculates maintenance cost for provided car number.
    
    Parameters:
        car (car): The car to use for maintenance calculation.

    Returns:
        float: Maintenance cost for provided car number.
    
    """
    return car.maintenance / 12
    
def calculate_loan(car, user_information):
    """
    
    Calculates loan when all configurations are done.
    
    parameters:
        car (car): The car to use for loan calculation.

    Returns:
        float: Loan amount.
    
    """
    principal_amount = car.expected_price - user_information.down_payment
    interest_rate = user_information.interest_rate / 12
    nbr_of_payments = 12
    return principal_amount * (interest_rate * (1 + interest_rate)**nbr_of_payments) / ((1 + interest_rate)**nbr_of_payments - 1)

def give_recommendation(menu_items):
    """
    
    Gives recommendation based on user configurations
    
    Parameters:
        menu_items (list): A list of booleans fow which menu items that has been done.
    
    Returns:
        None

    """
    if all(menu_items):
        gas_cost_car1 = calculate_gas_cost(cars[1], user_info)
        maintenance_car1 = calculate_maintenance(cars[1])
        loan_car1 = calculate_loan(cars[1], user_info)
        total_cost_car1 = gas_cost_car1 + maintenance_car1 + loan_car1

        gas_cost_car2 = calculate_gas_cost(cars[2], user_info)
        maintenance_car2 = calculate_maintenance(cars[2])
        loan_car2 = calculate_loan(cars[2], user_info)
        total_cost_car2 = gas_cost_car2 + maintenance_car2 + loan_car2

        car1_mention, car2_mention = '', ''
        if cars[1].make == cars[2].make:
            car1_mention = cars[1].model
            car2_mention = cars[2].model
        else:
            car1_mention = cars[1].make
            car2_mention = cars[2].make
        if total_cost_car1 < total_cost_car2:
            print(f"{cars[1].make} is recommended. Based on the following factors:")
        else:
            print(f"{cars[2].make} is recommended. Based on the following factors:")

        print("\nTOTAL COST:")
        print(f"{car1_mention} = {total_cost_car1:.2f}€")
        print(f"{car2_mention} = {total_cost_car2:.2f}€")

        print("\nGAS COST:")
        print(f"{car1_mention} = {gas_cost_car1:.2f}€")
        print(f"{car2_mention} = {gas_cost_car2:.2f}€")

        print("\nMAINTENANCE COST:")
        print(f"{car1_mention} = {maintenance_car1:.2f}€")
        print(f"{car2_mention} = {maintenance_car2:.2f}€")

        print("\nLOAN COST:")
        print(f"{car1_mention} = {loan_car1:.2f}€")
        print(f"{car2_mention} = {loan_car2:.2f}€")
    else:
        print("Please configure both cars and additional parameters.")
