def look_up_primes(max_val):
    """
    max_val: integer
    This function (as the name suggests) looks up prime numbers until {max_val} is reached.
    """
    prime_list = []
    for i in range(2, max_val):
        prime = True
        for y in range(2, i):
            if (i % y) == 0:
                prime = False
        if prime:
            prime_list.append(i)
    return prime_list


def float_to_binary(fraction):
    """
    fraction: float
    This functions returns a binary representation of a float.
    """
    binary_str = ''
    for index in range(32):
        fraction *= 2
        if fraction >= 1:
            binary_str += '1'
            fraction -= 1
        else:
            binary_str += '0'
    return binary_str
