class Customer:
    class_id = 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        result = Customer.class_id
        Customer.class_id += 1
        return result

    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'
