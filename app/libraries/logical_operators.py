def shift_right(value, shifts):
    """
    value : binary string
    shifts : integer
    This function will shift the binary representation ({shift} times) to the right.
    """
    shifts = shifts % len(value)
    rem_bits = value[:-shifts]
    zeros = ''
    for shift in range(0, shifts):
        zeros += '0'
    shifted_bits = zeros + rem_bits
    return shifted_bits


def right_rotate(value, rotations):
    """
    value : binary string
    rotations : integer
    This function will rotate the binary representation ({rotations} times) to the right.
    """
    value = str(value)
    rotations = rotations % len(value)
    rot_bits = value[-rotations:]  # Gets the last (-rotation) Bits
    remaining_bits = value[:-rotations]  # Gets the first (rotation) Bits
    rotated_bits = rot_bits + remaining_bits  # Last Bits added in front of the first bits
    return rotated_bits


def binary_negation(value):
    """
    value: binary string
    Loops through {value} and swaps every 1 with a 0
    return: string
    """
    value = str(value)
    inverse_str = ''
    for i in value:
        if i == '1':
            inverse_str += '0'
        else:
            inverse_str += '1'
    return inverse_str


def byte_and(value_1, value_2):
    """
    value_1: str or int
    value_2: str or int
    output: str
    """
    value_1 = int(value_1, 2) if isinstance(value_1, str) else value_1
    value_2 = int(value_2, 2) if isinstance(value_2, str) else value_2

    result = value_1 & value_2

    return bin(result)[2:]


def xor(x1, x2):
    """
    x1: binary string
    x2: binary string
    This function creates a new string where a 1 is added when two values are different. (Xor)
    """
    if not (set(x1) <= {'0', '1'} and set(x2) <= {'0', '1'}):
        raise ValueError("Input must be a binary string!")

    bin_length = max(len(x1), len(x2))

    x1 = x1.zfill(bin_length)
    x2 = x2.zfill(bin_length)

    xor_result = ''

    for q in range(bin_length):
        if x1[q] == x2[q]:
            xor_result += '0'
        else:
            xor_result += '1'

    return xor_result


def add_binary(bin1, bin2):
    """
    bin1: binary string
    bin2: binary string
    This function adds two binary strings together.
    """
    bin_length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(bin_length)
    bin2 = bin2.zfill(bin_length)

    binary_result = ''
    carry = 0

    for q in range(bin_length - 1, -1, -1):
        temp_value = int(bin1[q]) + int(bin2[q]) + carry
        bit_sum = temp_value % 2
        carry = temp_value // 2
        binary_result = str(bit_sum) + binary_result

    if carry:
        binary_result = '1' + binary_result

    return binary_result
