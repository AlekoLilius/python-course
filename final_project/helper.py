import user_input as uinput
import user_information as uinfo
import car
import web_handler

# Initializing data variables
cars = {}
user_info = None

def configure_car(car_nbr):
    """Configures a car based on user input and car number."""
    make, model, year, mileage, fuel_efficiency = uinput.get_vehicle_details()
    expected_price = uinput.get_expected_price()
    maintenance = uinput.get_maintenance(model)

    vehicle = car.Car(car_nbr, make, model, year, mileage, fuel_efficiency, expected_price, maintenance)
    cars[car_nbr] = vehicle
    return True

def configure_user():
    """Configures user based on user input"""
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


def calculate_gas_cost(car_nbr):
    """Calculates gas cost for provided car number."""
    return (cars[car_nbr].fuel_efficiency * sum(user_info.driving_habits)) / 12

def calculate_maintenance(car_nbr):
    """Calculates maintenance cost for provided car number."""
    return cars[car_nbr].maintenance / 12
    
def calculate_loan(car_nbr):
    """Calculates loan when all configurations are done"""
    principal_amount = cars[car_nbr].expected_price - user_info.down_payment
    interest_rate = user_info.interest_rate / 12
    nbr_of_payments = 12
    return principal_amount * (interest_rate * (1 + interest_rate)**nbr_of_payments) / ((1 + interest_rate)**nbr_of_payments - 1)

def give_recommendation(menu_items):
    """Gives recommendation based on user configurations"""
    if all(menu_items):
        gas_cost_car1 = calculate_gas_cost(1)
        maintenance_car1 = calculate_maintenance(1)
        loan_car1 = calculate_loan(1)
        total_cost_car1 = gas_cost_car1 + maintenance_car1 + loan_car1

        gas_cost_car2 = calculate_gas_cost(2)
        maintenance_car2 = calculate_maintenance(2)
        loan_car2 = calculate_loan(2)
        total_cost_car2 = gas_cost_car2 + maintenance_car2 + loan_car2

        if total_cost_car1 < total_cost_car2:
            print(f"{cars[1].model} is recommended.")
        else:
            print(f"{cars[2].model} is recommended.")
    else:
        print("Please configure both cars and additional parameters.")
