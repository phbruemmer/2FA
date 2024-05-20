import logical_operators as lo


def remove_single_bits(value, length):
    """
    value : binary string
    length : needed length
    This function will remove the first bits of every binary representation
    if the length is smaller than the actual binary length.
    """
    if len(value) > length:
        removable_bit_amount = len(value) - length
        value = value[removable_bit_amount:]
    return value


def sigma_zero(w_value):
    """
    This function creates the correct sigma zero binary representation.
    binary:
        - right rotate 7
        - right rotate 18
        - right shift 3
    """
    rr7 = int(lo.right_rotate(w_value, 7).zfill(32), 2)
    rr18 = int(lo.right_rotate(w_value, 18).zfill(32), 2)
    rs3 = int(lo.shift_right(w_value, 3).zfill(32), 2)

    return format((rr7 ^ rr18 ^ rs3), '032b')


def sigma_one(w_value):
    """
    This function creates the correct sigma one binary representation.
    binary:
        - right rotate 17
        - right rotate 19
        - right shift 10
    """
    rr17 = lo.right_rotate(w_value, 17).zfill(32)
    rr19 = lo.right_rotate(w_value, 19).zfill(32)
    rs10 = lo.shift_right(w_value, 10).zfill(32)
    temp_val = lo.xor(rr17, rr19)
    return lo.xor(temp_val, rs10)


def sigma_one_hashing(e):
    """
    e: binary string
    """
    e1 = lo.right_rotate(e, 6)
    e2 = lo.right_rotate(e, 11)
    e3 = lo.right_rotate(e, 25)
    temp_e = lo.xor(e1, e2)
    e4 = lo.xor(temp_e, e3)
    return e4


def sigma_zero_hashing(a):
    """
    a: binary string
    """
    a1 = lo.right_rotate(a, 2)
    a2 = lo.right_rotate(a, 13)
    a3 = lo.right_rotate(a, 22)
    temp_a = lo.xor(a1, a2)
    a4 = lo.xor(temp_a, a3)
    return a4


def choice(e, f, g):
    """
    e, f, g: binary
    """
    e = e.zfill(32)
    f = f.zfill(32)
    g = g.zfill(32)
    not_e = lo.binary_negation(e)
    choice_1 = lo.byte_and(e, f).zfill(32)
    choice_2 = lo.byte_and(not_e, g).zfill(32)
    result = lo.xor(choice_1, choice_2)
    return result  # Return result as binary string


def majority(a, b, c):
    """
    a, b, c: binary
    """
    bin_length = max(len(a), len(b), len(c))

    a = a.zfill(bin_length)
    b = b.zfill(bin_length)
    c = c.zfill(bin_length)

    maj_1 = lo.byte_and(a, b)
    maj_2 = lo.byte_and(a, c)
    maj_3 = lo.byte_and(b, c)
    temp_xor = lo.xor(maj_1, maj_2)

    return lo.xor(temp_xor, maj_3)
