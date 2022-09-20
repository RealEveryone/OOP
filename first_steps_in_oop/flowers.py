class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = int(water_requirements)
        self.is_happy = False

    def is_flower_happy(self):
        string = 'is not happy'
        if self.is_happy:
            string = 'is happy'
        return string

    def water(self, value):
        if value >= self.water_requirements:
            self.is_happy = True

    def status(self):
        return f'{self.name} {self.is_flower_happy()}'


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())