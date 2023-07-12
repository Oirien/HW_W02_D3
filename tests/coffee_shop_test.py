import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100)
        self.drink = Drink("Cola", 2, 15)
        self.customer = Customer("Steve", 50, 45, 65)
    
    #testing class name
    # @unittest.skip("delete this line to run the test")
    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)


    # @unittest.skip("delete this line to run the test")

    # testing for till value
    # @unittest.skip("delete this line to run the test")
    def test_coffee_shop_has_till(self):
        self.assertEqual(100, self.coffee_shop.till)

    # @unittest.skip("delete this line to run the test")
    def test_increase_till(self):
        self.coffee_shop.increase_till(10)
        self.assertEqual(110, self.coffee_shop.till)

    # @unittest.skip("delete this line to run the test")
    def test_decrease_till(self):
        self.coffee_shop.decrease_till(10)
        self.assertEqual(90, self.coffee_shop.till)

    def test_sell_drink(self):
        self.coffee_shop.sell_drink(self.customer, self.drink.price)
        self.assertEqual(102, self.coffee_shop.till)
        self.assertEqual(48, self.customer.wallet)

    def test_age_check(self):
        self.assertEqual(True, self.coffee_shop.age_check(self.customer))

    def test_dict_of_drinks(self):
        self.coffee_shop.dict_of_drinks(self.drink)
        self.assertDictEqual({"name": "Cola", "price": 2}, self.coffee_shop.drinks)

    def test_customer_can_afford(self):
        self.coffee_shop.dict_of_drinks(self.drink)
        self.assertEqual("Col", self.coffee_shop.customer_can_afford(self.customer, self.coffee_shop.drinks))
