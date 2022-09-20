from project.product import Product


class ProductRepository:
    products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for current in self.products:
            if current.name == product_name:
                return current

    def remove(self, product_name):
        for current in self.products:
            if current.name == product_name:
                self.products.remove(current)

    def __repr__(self):
        output = ''
        for current_product in self.products:
            output += f"{current_product.name}: {current_product.quantity}\n"
        return output.strip()