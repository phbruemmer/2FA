def create_k_constants():
    def look_up_primes(max_val):
        """
        max_val: integer
        This function (as the name suggests) looks up prime numbers until {max_val} is reached.
        It starts by looping through the numbers from 2 to {max_val} - Every loop starts another for loop that
        loops through the numbers from 2 to the current number.
        If the current number divided by the current number in the second loop has no leftovers, the current
        number is not a prime number.
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
    # 312 -> First 64 prime numbers -> 2..311
    prime_numbers = look_up_primes(312)
    k = []

    for num in prime_numbers:
        cube_root_num = num ** (1 / 3)
        rounded_down = int(cube_root_num)
        fraction_num = cube_root_num - rounded_down
        k.append(float_to_binary(fraction_num))

    return k

