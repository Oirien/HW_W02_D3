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
		if self.age_check == False:
			return
		customer.buy_drink(drink)
		self.increase_till(drink)

	def age_check(self, customer):
		return bool(customer.age >= 16)