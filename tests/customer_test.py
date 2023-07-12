import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    
    # @unittest.skip("delete this line to run the test")
    def setUp(self):
        self.customer = Customer("Steve", 50, 45, 65)
        self.drink = Drink("Cola", 2.1, 15)
    # @unittest.skip("delete this line to run the test")
    def test_customer_has_name(self):
        self.assertEqual("Steve", self.customer.name)
    # @unittest.skip("delete this line to run the test")    
    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)
    # @unittest.skip("delete this line to run the test")
    def test_customer_has_age(self):
        self.assertEqual(45, self.customer.age)
    # @unittest.skip("delete this line to run the test")
    def test_customer_has_energy(self):
        self.assertEqual(65, self.customer.energy)

    def test_decrease_wallet(self):
        self.customer.decrease_wallet(10)
        self.assertEqual(40, self.customer.wallet)

    def test_increase_energy(self):
        self.customer.increase_energy(self.drink.caffiene_level)
        self.assertEqual(80, self.customer.energy)

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink.price)
        self.assertEqual(47.9, (self.customer.wallet))

    def test_energy_level(self):
        self.assertEqual(True, self.customer.energy_level(self.customer))
        