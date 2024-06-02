
class Car:
    def __init__(self, id, make, model, year, mileage, fuel_efficiency, expected_price, maintenance):
        """
        
        Initializes car object.
        
        Parameters:
            id (int): The car id.
            make (str): The car make.
            model (str): The car model.
            year (int): The car year.
            mileage (int): The car mileage.
            fuel_efficiency (float): The car fuel efficiency.
            expected_price (int): The car expected price.
            maintenance (int): The car maintenance.
        
        Returns:
            None
        """

        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_efficiency = fuel_efficiency
        self.expected_price = expected_price
        self.maintenance = maintenance
    
    def __str__(self):
        """
        
        Returns car details.

        Returns:
            str
        
        """
        return f"{self.make} {self.model} {self.year} {self.mileage} {self.fuel_efficiency} {self.expected_price} {self.maintenance}"