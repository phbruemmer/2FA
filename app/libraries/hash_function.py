
"""
- - - - - - - - - - -
Hashfunction - Encryption
- - - - - - - - - - -

Hashfunction are functions to encrypt data and to securely decrypt data.
The function creates a code (for example 256 Bits long) and encrypts the data with it.
The Code is always the same for the same text but will change if you change something.
"""


def sha256(data):
    print(data)
    binary_list = []
    # Convert Data to Binary using ASCII
    for i in data:
        binary_data = bin(ord(i))
        binary_list.append(binary_data)
    # Get bitwise length of data input
    data_binary_len = len(binary_list) * 8

    # calculate zeros to append
    k_bit_len = 896 - (data_binary_len + 1)

    binary_zero_bits = 0b1

    """
    masked_number = binary_zero_bits & ((1 << k_bit_len) - 1)
    padded_number = masked_number << (k_bit_len - binary_zero_bits.bit_length())
    print(bin(padded_number))
    """


    print(binary_zero_bits)


sha256('abc')

