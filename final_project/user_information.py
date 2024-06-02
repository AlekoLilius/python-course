
class UserInformation:
    def __init__(self, driving_habits, interest_rate, down_payment):
        """
        Initializes a new instance of the UserInformation class.

        Parameters:
            driving_habits (list): A list of integers representing the user's driving habits.
            interest_rate (float): The interest rate for the car loan.
            down_payment (int): The down payment for the car purchase.

        Returns:
            None
        """
        self.driving_habits = driving_habits
        self.interest_rate = interest_rate
        self.down_payment = down_payment
        self.car1 = None
        self.car2 = None

    def __str__(self):
        """
        
        Returns user information.  

        Returns:
            str
        
        """
        return f"{self.driving_habits} {self.expected_price} {self.interest_rate} {self.down_payment} {self.car1} {self.car2}"
    
    def set_car(self, nbr, car): 
        """
        
        Sets car for provided car number.

        Parameters:
            nbr (int): The car number to set.
            car (Car): The car object to set.

        Returns:
            None
        
        """
        if nbr == 1:
            self.car1 = car
        elif nbr == 2:
            self.car2 = car

    def update_info(self, new_driving_habits, new_interest_rate, new_down_payment):
        """
        
        Updates user info

        Parameters:
            new_driving_habits (list): A list of integers representing the user's driving habits.
            new_interest_rate (float): The interest rate for the car loan.
            new_down_payment (float): The down payment for the car purchase.

        Returns:
            None
        """
        self.driving_habits = new_driving_habits
        self.interest_rate = new_interest_rate
        self.down_payment = new_down_payment