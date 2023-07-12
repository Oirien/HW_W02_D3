class Customer:
    def __init__(self, name, wallet, age, energy):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy = energy

    def decrease_wallet(self, amount):
        self.wallet -= amount
        

    def buy_drink(self, drink):
        self.wallet -= drink

    def energy_level(self, customer):
        return bool(customer.energy > 50)