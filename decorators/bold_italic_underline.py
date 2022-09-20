def make_underline(func):
    def wrapped(*args):
        result = func(*args)
        return f'<u>{result}</u>'

    return wrapped


def make_italic(func):
    def wrapped(*args):
        result = func(*args)
        return f'<i>{result}</i>'

    return wrapped


def make_bold(func):
    def wrapped(*args):
        result = func(*args)
        return f'<b>{result}</b>'

    return wrapped




@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))