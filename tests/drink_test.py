import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    @unittest.skip("delete this line to run the test")
    def setUp(self):
        self.drink = Drink("Cola", 2.1, 15)
    @unittest.skip("delete this line to run the test")
    def test_drink_has_name(self):
        self.assertEqual("Cola", self.drink.name)
    @unittest.skip("delete this line to run the test")
    def test_drink_has_price(self):
        self.assertEqual(2.1, self.drink.price)
    @unittest.skip("delete this line to run the test")
    def test_drink_has_caffiene_level(self):
        self.assertEqual(15, self.drink.caffiene_level)