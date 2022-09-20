def even_parameters(func):

    def is_even(*args):

        if len([x for x in args if isinstance(x, int) and x % 2 == 0]) == len(args):
            return True

        return False

    def wrapped(*args):
        if is_even(*args):
            return func(*args)
        return "Please use only even numbers!"

    return wrapped


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))