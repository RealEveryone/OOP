from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.air_con = 0.9

    def drive(self, distance):
        spent_fuel = distance * (self.fuel_consumption + self.air_con)
        if spent_fuel > self.fuel_quantity:
            return
        self.fuel_quantity -= spent_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.air_con = 1.6

    def drive(self, distance):
        spent_fuel = distance * (self.fuel_consumption + self.air_con)
        if spent_fuel > self.fuel_quantity:
            return
        self.fuel_quantity -= spent_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)