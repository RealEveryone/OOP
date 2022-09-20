def cache(func):
    cached_values = {}

    def wrapped(value):
        if value not in cached_values:
            cached_values[value] = func(value)
        wrapped.log = cached_values
        return cached_values[value]

    return wrapped


@cache
def fibonacci(n):
    log = 2
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)


fibonacci(3)
print(fibonacci.log)
