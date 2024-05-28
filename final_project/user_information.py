
class UserInformation:
    def __init__(self, driving_habits, interest_rate, down_payment):
        self.driving_habits = driving_habits
        self.interest_rate = interest_rate
        self.down_payment = down_payment
        self.car1 = None
        self.car2 = None

    def __str__(self):
        """Prints user info"""
        return f"{self.driving_habits} {self.expected_price} {self.interest_rate} {self.down_payment} {self.car1} {self.car2}"
    
    def set_car(self, nbr, car): 
        """Sets car based on car number"""
        if nbr == 1:
            self.car1 = car
        elif nbr == 2:
            self.car2 = car

    def update_info(self, new_driving_habits, new_interest_rate, new_down_payment):
        """Updates user info"""
        self.driving_habits = new_driving_habits
        self.interest_rate = new_interest_rate
        self.down_payment = new_down_payment