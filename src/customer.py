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
        self.increase_energy(drink)

    def increase_energy(self, drink):
        self.energy += drink

    def energy_level(self, customer):
        return bool(customer.energy > 50)
    
    def decrease_energy(self, food):
        self.energy -= food

    def buy_food(self, food, foodenergy):
        self.wallet -= food
        self.decrease_energy(foodenergy)