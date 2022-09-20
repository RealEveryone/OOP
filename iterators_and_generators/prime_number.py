def is_prime(number):
    if number <= 1:
        return False

    is_prime = True

    for i in range(2, number):
        if number % 2 == 0:
            is_prime = False
            break
    return is_prime


def get_primes(integer_list):
    for number in integer_list:
        if is_prime(number):
            yield number
