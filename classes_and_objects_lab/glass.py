class Glass:
    def __init__(self):
        self.content = 0
        self.capacity = 250

    def fill(self, ml):
        if ml + self.content <= self.capacity:
            self.content += ml
            return f'Glass filled with {ml} ml'
        return f'Cannot add {ml} ml'

    def empty(self):
        self.content = 0
        return 'Glass is now empty'

    def info(self):
        return f'{self.capacity - self.content} ml left'



print(Glass.capacity)