import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    
    # @unittest.skip("delete this line to run the test")
    def setUp(self):
        self.food = Food("Pizza", 5, 25)
    # @unittest.skip("delete this line to run the test")
    def test_food_has_name(self):
        self.assertEqual("Pizza", self.food.name)
    # @unittest.skip("delete this line to run the test")
    def test_food_has_price(self):
        self.assertEqual(5, self.food.price)
    # @unittest.skip("delete this line to run the test")
    def test_food_has_digestion_level(self):
        self.assertEqual(25, self.food.digestion_level)