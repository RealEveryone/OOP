from itertools import permutations


def possible_permutations(elements):
    x = permutations(elements)
    for result in x:
        yield list(result)
