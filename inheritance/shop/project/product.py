class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity: int):
        def difference():
            return self.quantity - quantity

        self.quantity -= quantity if difference() >= 0 else 0

    def increase(self, quantity: int):
        self.quantity += quantity

    def __repr__(self):
        return self.name



