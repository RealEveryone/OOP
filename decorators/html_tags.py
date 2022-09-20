def tags(param):
    def decorator(func):
        def wrapped(*args):
            result = func(*args)
            return f'<{param}>{result}</{param}>'

        return wrapped

    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))