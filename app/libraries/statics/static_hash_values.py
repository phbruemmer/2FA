from . import static_value_calculations as svc


def create_k_constants():
    # 312 -> First 64 prime numbers -> 2..311
    prime_numbers = svc.look_up_primes(312)
    k = []

    for num in prime_numbers:
        cube_root_num = num ** (1 / 3)
        rounded_down = int(cube_root_num)
        fraction_num = cube_root_num - rounded_down
        k.append(svc.float_to_binary(fraction_num))
    return k


def create_h_constants():
    # 312 -> First 64 prime numbers -> 2..311
    prime_numbers = svc.look_up_primes(20)
    k = []

    for num in prime_numbers:
        cube_root_num = num ** (1 / 2)
        rounded_down = int(cube_root_num)
        fraction_num = cube_root_num - rounded_down
        k.append(svc.float_to_binary(fraction_num))

    return k

