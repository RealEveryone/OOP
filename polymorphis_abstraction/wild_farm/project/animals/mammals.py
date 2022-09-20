from project.animals.animal import Mammal


class Mouse(Mammal):
    @property
    def weight_incremental(self):
        return 0.10

    @property
    def possible_food(self):
        return ['Vegetable', 'Fruit']

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal):
    @property
    def weight_incremental(self):
        return 0.40

    @property
    def possible_food(self):
        return ['Meat']

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):
    @property
    def weight_incremental(self):
        return 0.30

    @property
    def possible_food(self):
        return ['Vegetable', 'Meat']

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):
    @property
    def weight_incremental(self):
        return 1

    @property
    def possible_food(self):
        return ['Meat']

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'ROAR!!!'
