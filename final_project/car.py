
class Car:
    def __init__(self, id, make, model, year, mileage, fuel_efficiency, expected_price, maintenance):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_efficiency = fuel_efficiency
        self.expected_price = expected_price
        self.maintenance = maintenance
    
    def __str__(self):
        """Prints car details"""
        return f"{self.make} {self.model} {self.year} {self.mileage} {self.fuel_efficiency} {self.expected_price} {self.maintenance}"