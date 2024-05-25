from datetime import datetime
import pyfiglet

# Initialize global variables
cart_value = 0
delivery_distance = 0
number_of_items = 0
order_time = ''
surcharge = 0
FREE_DELIVERY_THRESHOLD = 200.0

# Function to calculate surcharge based on cart value and number of items
def calculate_surcharge(cart_value, number_of_items):
    
    item_surcharge, small_order_surcharge = 0, 0

    # Small order surcharge if cart value is less than 10
    if cart_value < 10:
        small_order_surcharge = 10 - cart_value
    else:
        small_order_surcharge = 0

    # Item surcharge if number of items is 5 or more
    if number_of_items >= 5:
        item_surcharge = (number_of_items - 4) * 0.50

    # Additional bulk fee if number of items is more than 12
    if number_of_items > 12:
        item_surcharge += 1.20

    return small_order_surcharge + item_surcharge

# Function to validate the datetime string format
def datetime_valid(dt_str):

    try:
        datetime.fromisoformat(dt_str)
    except ValueError:
        return False
    return True

# Function to calculate the distance fee based on delivery distance
def distance_fee(delivery_distance):

    BASE_FEE = 2.0
    ADDITIONAL_DISTANCE_FEE = 1.0
    
    # Base fee for distances up to 1000 meters
    if delivery_distance <= 1000:
        return BASE_FEE
    else:
        # Additional fee for every 500 meters beyond 1000 meters
        return BASE_FEE + ADDITIONAL_DISTANCE_FEE * ((delivery_distance - 1000 + 499) // 500)

# Function to check if the order time is during the Friday rush hour
def friday_rush(order_time):

    RUSH_HOUR_MULTIPLIER = 1.2
    order_dt = datetime.fromisoformat(order_time)
    
    # Friday rush hour from 15:00 to 19:00
    if order_dt.weekday() == 4 and 15 <= order_dt.hour < 19:
        return RUSH_HOUR_MULTIPLIER
    return 1.0

# Function to calculate the total delivery fee
def calculate_total_delivery_fee(cart_value, delivery_distance, item_count, order_time):

    MAX_DELIVERY_FEE = 15.0
    FREE_DELIVERY_THRESHOLD = 200.0

    # Free delivery if cart value exceeds the threshold
    if cart_value >= FREE_DELIVERY_THRESHOLD:
        return 0.0

    # Calculate surcharges and distance fee
    surcharge = calculate_surcharge(cart_value, item_count)
    distance_fee_value = distance_fee(delivery_distance)

    total_fee = surcharge + distance_fee_value

    # Apply Friday rush hour multiplier if applicable
    total_fee *= friday_rush(order_time)

    # Cap the total fee at the maximum delivery fee
    total_fee = min(total_fee, MAX_DELIVERY_FEE)

    return round(total_fee, 2)

# Main function to interact with the user and calculate delivery fee
def main():
    print(r'''
          
 __          __  _                            _          _   _                _      _ _                         __                      _            _       _                 
 \ \        / / | |                          | |        | | | |              | |    | (_)                       / _|                    | |          | |     | |              _ 
  \ \  /\  / ___| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___    __| | ___| |___   _____ _ __ _   _  | |_ ___  ___    ___ __ _| | ___ _   _| | __ _| |_ ___  _ __  (_)
   \ \/  \/ / _ | |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \  / _` |/ _ | | \ \ / / _ | '__| | | | |  _/ _ \/ _ \  / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|    
    \  /\  |  __| | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/ | (_| |  __| | |\ V |  __| |  | |_| | | ||  __|  __/ | (_| (_| | | (__| |_| | | (_| | || (_) | |     _ 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___|  \__,_|\___|_|_| \_/ \___|_|   \__, | |_| \___|\___|  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|    (_)
                                                                                                         __/ |                                                                  
                                                                                                        |___/                                                                   
''')

    while True:
        try:
            # Get cart value
            cart_value = int(input('Enter cart value (in cents): ')) / 100
            break
        except ValueError as e:
            print("Invalid input, please try again.\n")
            continue
    
    while True:
        try:
            # Get delivery distance
            delivery_distance = int(input('Enter delivery distance (in meters): '))
            break
        except ValueError as e:
            print("Invalid input, please try again.\n")
            continue
    while True:
        try:
            # Get number of items
            number_of_items = int(input('Enter the number of items: '))
            break
        except ValueError as e:
            print("Invalid input, please try again.\n")
            continue

    while True:
        # Get and validate order time
        order_time = input('Enter the order time (YYYY-MM-DD HH:MM:SS): ')
        if not datetime_valid(order_time):
            print('Invalid datetime format, please try again.\n')
            continue
        else:
            break

    # Calculate and display the delivery fee
    delivery_fee = calculate_total_delivery_fee(cart_value, delivery_distance, number_of_items, order_time)
    delivery_fee_str = f"{delivery_fee:.2f} Euro"
    ascii_art_delivery_fee = pyfiglet.figlet_format("Delivery Fee:")
    ascii_art_fee_amount = pyfiglet.figlet_format(delivery_fee_str)

    # Display the fee with ASCII art
    print('')
    print(ascii_art_delivery_fee)
    print(ascii_art_fee_amount)

    print('''

  _______ _                 _                           __             _____       _ _                  ______           _____      _            _       _             
 |__   __| |               | |                         / _|           |  __ \     | (_)                |  ____|         / ____|    | |          | |     | |            
    | |  | |__   __ _ _ __ | | __  _   _  ___  _   _  | |_ ___  _ __  | |  | | ___| |___   _____ _ __  | |__ ___  ___  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
    | |  | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | | |  _/ _ \| '__| | |  | |/ _ \ | \ \ / / _ \ '__| |  __/ _ \/ _ \ | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | |  | | | | (_| | | | |   <  | |_| | (_) | |_| | | || (_) | |    | |__| |  __/ | |\ V /  __/ |    | | |  __/  __/ | |___| (_| | | (__| |_| | | (_| | || (_) | |   
    |_|  |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_| |_| \___/|_|    |_____/ \___|_|_| \_/ \___|_|    |_|  \___|\___|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                    __/ |                                                                                                                              
                                   |___/                                                                                                                               

''')

# Entry point of the script
if __name__ == '__main__':
    main()