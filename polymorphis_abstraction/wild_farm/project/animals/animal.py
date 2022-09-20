from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def weight_incremental(self):
        pass

    @property
    @abstractmethod
    def possible_food(self):
        pass

    def feed(self, food: Food):
        type_of_food = food.__class__.__name__
        if type_of_food not in self.possible_food:
            return f'{self.__class__.__name__} does not eat {type_of_food}!'
        self.weight += food.quantity * self.weight_incremental
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def make_sound(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def make_sound(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
