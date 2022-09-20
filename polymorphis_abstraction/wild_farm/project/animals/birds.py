from project.animals.animal import Bird


class Owl(Bird):
    @property
    def weight_incremental(self):
        return 0.25

    @property
    def possible_food(self):
        return ['Meat']

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):
    @property
    def weight_incremental(self):
        return 0.35

    @property
    def possible_food(self):
        return ['Vegetable', 'Meat', 'Fruit', 'Seed']

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'
