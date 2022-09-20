class Cup:
    def __init__(self, cup_size, initial_quantity):
        self.size = cup_size
        self.quantity = initial_quantity

    def fill(self, volume):
        self.quantity += volume if (self.quantity + volume) < self.size else 0

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
