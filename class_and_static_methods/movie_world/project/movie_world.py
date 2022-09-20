from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __number_of_customers(self):
        return len(self.customers)

    def __number_of_dvds(self):
        return len(self.dvds)

    def __find_customer(self, id):
        for customer in self.customers:
            if customer.id == id:
                return customer

    def __find_dvd(self, id):
        for dvd in self.dvds:
            if dvd.id == id:
                return dvd

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if self.__number_of_customers() < 10:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if self.__number_of_dvds() < 15:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__find_customer(customer_id)
        dvd = self.__find_dvd(dvd_id)
        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'
        if dvd.is_rented:
            return 'DVD is already rented'
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__find_customer(customer_id)
        dvd = self.__find_dvd(dvd_id)

        if dvd not in customer.rented_dvds:
            return f'{customer.name} does not have that DVD'

        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f'{customer.name} has successfully returned {dvd.name}'

    def __repr__(self):
        output = ''
        for customer in self.customers:
            output += customer.__repr__() + '\n'
        for movies in self.dvds:
            output += movies.__repr__() + '\n'
        return output.strip()


