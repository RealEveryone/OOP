def logged(function):
    def wrapped(*args):
        result = function(*args)
        return f'you called {function.__name__}({", ".join(str(x) for x in args)})\nit returned {result}'
    return wrapped


@logged
def func(*args):
    return 3 + len(args)

print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))