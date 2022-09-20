def fibonacci():
    first_num = 0
    second = 1
    yield first_num
    yield second

    while True:
        result = first_num + second
        first_num , second = second, result
        yield result