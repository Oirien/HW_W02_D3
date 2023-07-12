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
		if customer.energy_level == True:
			return
		customer.buy_drink(drink)
		self.increase_till(drink)

	def age_check(self, customer):
		return bool(customer.age >= 16)
	
	def dict_of_drinks(self, drink):
		self.drinks.update({
			"name": drink.name, 
			"price": drink.price,
			"quantity": drink.quantity
		})

	def customer_can_afford(self, customer, drinks):
		drinks_customer_can_afford = []
		if "price" in drinks.keys():
			if drinks["price"] < customer.wallet:
				drinks_customer_can_afford.append(drinks["name"])
		return drinks_customer_can_afford
	
	def stock_add(self, drink, amount):
		if "quantity" in drink.keys():
			drink["quantity"] += amount