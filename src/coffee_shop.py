class CoffeeShop:
	def __init__(self, name, till):
		self.name = name
		self.till = till
		self.drinks = {}

	def increase_till(self, amount):
		self.till += amount

	def decrease_till(self, amount):
		self.till -= amount

	def sell_drink(self, customer, drink):
		customer.buy_drink(drink)
		self.increase_till(drink)