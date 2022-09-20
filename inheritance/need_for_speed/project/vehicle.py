class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        used_fuel = kilometers * self.fuel_consumption

        def difference():
            return self.fuel - used_fuel

        self.fuel -= used_fuel if difference() >= 0 else 0