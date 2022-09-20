class dictionary_iter:

    def __init__(self, data):
        self.dictionary = data
        self.idx = (pair for pair in self.dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.idx)
