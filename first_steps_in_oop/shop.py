class Shop:
    def __init__(self, name, ll):
        self.items = ll
        self.name = name

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])

print(shop.get_items_count())
