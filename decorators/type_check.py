def type_check(data_type):

    def decorator(func):
        def wrapper(*args):
            for current in args:
                if not isinstance(current, data_type):
                    return 'Bad Type'
            result = func(*args)
            return result

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
