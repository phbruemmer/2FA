
"""
- - - - - - - - - - -
Hashfunction - Encryption
- - - - - - - - - - -

Hashfunction are functions to encrypt data and to securely decrypt data.
The function creates a code (for example 256 Bits long) and encrypts the data with it.
The Code is always the same for the same text but will change if you change something.
"""

def get_bin(binary_data):
    binary_data = binary_data.replace(' ', '')
    i = 0
    data_str = ''
    data_list = []
    for data in binary_data:
        print(data)
        data_str += data
        if (i % 8) == 0:
            data_list.append(data_str)
            data_str = ''
    return data_list


def compare(data):
    result = True
    bin_to_compare = get_bin("""
    01100110 01100100 01110011 01101010
    01101011 01100001 01100110 01101010
    01101011 01101100 01100001 01110011
    01100100 01101010 01101011 01101100
    01100001 01101010 01110011 01101011
    01101100 11000011 10110110 01100110
    01101010 01101011 01101100 01100100
    01100001 01110011 01101010 01101011
    01101100 01100110 01101010 01100001
    01100100 01101011 01110011 11000011
    10110110 01100110 01101010 01101100
    01101011 01100001 01101010 01101010
    01101010 01101010 01101010 01101010
    01101010 01101010 00110100 00110100
    """)

    for i in range(0, len(data)):
        if not bin_to_compare[i] == data[i]:
            print(data[i])
            print(bin_to_compare[i])
            result = False

    return result


def sha256(data):
    """print(data)
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


    masked_number = binary_zero_bits & ((1 << k_bit_len) - 1)
    padded_number = masked_number << (k_bit_len - binary_zero_bits.bit_length())
    print(bin(padded_number))


    print(binary_zero_bits)
    """
    print(data)

    binary_list = []
    for i in data:
        binary_data = bin(ord(i))
        binary_list.append(binary_data)

    # Convert Data to Binary using ASCII
    # Get bitwise length of data input
    # Append single one at the end
    binary_list.append(0b10000000)
    data_binary_len = len(binary_list)
    i = 0

    # print(len(binary_list))

    i = 512
    while data_binary_len + 64 > i:
        i = i * 2
    print(i)
    if compare(binary_list):
        print('Nothing wrong here i guess')
    else:
        print('Something is wrong here')


sha256('fdsjkafjklasdjklajsklöfjkldasjklfjadksöfjlkajjjjjjjj44')

