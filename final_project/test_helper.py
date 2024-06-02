import unittest
import helper
import car
import user_information as uinfo

class TestHelper(unittest.TestCase):
    ''''''
    test_car1 = car.Car(1, "Toyota", "Toyota Crown", 2015, 15000, 40.5, 17000, 7000)
    test_car2 = car.Car(2, "Audi", "Audi A6", 2018, 12000, 34.2, 20000, 6600)
    test_user_info = uinfo.UserInformation([45, 23], 0.04, 5000)
    def test_calculate_gas_cost(self):
        '''
        
        Check if gas cost is calculated correctly.
        
        '''
        self.assertAlmostEqual(helper.calculate_gas_cost(self.test_car1, self.test_user_info), 229.50)
        self.assertAlmostEqual(helper.calculate_gas_cost(self.test_car2, self.test_user_info), 193.80)
    
    def test_calculate_maintenance(self):
        '''
        
        Check if maintenance is calculated correctly.
        
        '''
        self.assertAlmostEqual(helper.calculate_maintenance(self.test_car1), 583.3333333333333)
        self.assertAlmostEqual(helper.calculate_maintenance(self.test_car2), 550)

    def test_calculate_loan(self):
        '''
        
        Check if loan is calculated correctly.
        
        '''
        self.assertAlmostEqual(helper.calculate_loan(self.test_car1, self.test_user_info), 1021.798850346672)
        self.assertAlmostEqual(helper.calculate_loan(self.test_car2, self.test_user_info), 1277.2485629333398)