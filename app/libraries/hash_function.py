
"""
- - - - - - - - - - -
Hashfunction - Encryption
- - - - - - - - - - -

Hashfunction are functions to encrypt data and to securely decrypt data.
The function creates a code (for example 256 Bits long) and encrypts the data with it.
The Code is always the same for the same text but will change if you change something.
"""


DEBUG = True


def get_bin(binary_data):
    binary_data = binary_data.replace(' ', '')
    binary_data = binary_data.replace('\n', '')
    print(f'DEBUG - get_bin() -> {binary_data}')
    i = 0
    data_str = ''
    data_list = []
    for data in binary_data:
        data_str += data
        i += 1
        if (i % 8) == 0:
            data_list.append(data_str)
            data_str = ''

    print(f'DEBUG - get_bin() -> {len(data_list)}')
    print(f'DEBUG - get_bin() -> {len(data_list) * 8}')
    return data_list


def compare(data):
    result = True
    bin_to_compare = get_bin("""
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
01000001 01000001 01000001 01000001
10000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000""")
    print(f'DEBUG - compare() -> {bin_to_compare}')

    failed_list = []

    for i in range(0, len(data)):
        if DEBUG:
            print(data[i])
            # print(bin_to_compare[i])
            print(i)
        """if not bin_to_compare[i] == data[i]:
            failed_list.append([bin_to_compare[i], data[i], i])
            result = False"""
    print(failed_list)

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
        binary_data = format(ord(i), '08b')
        binary_list.append(binary_data)
        if DEBUG:
            print(binary_data)

    CONST_DATA_LEN = len(binary_list) * 8

    # Convert Data to Binary using ASCII
    # Get bitwise length of data input
    # Append single one at the end
    binary_list.append(format(128, '08b'))
    data_binary_len = len(binary_list)

    print(binary_list)

    print(f'DEBUG - data_binary_len -> {data_binary_len}')
    data_bit_len = data_binary_len * 8
    print(f'DEBUG - data_bit_len -> {data_bit_len}')

    i = 512
    CONST_I = 512

    while data_bit_len + 64 >= i:
        i += CONST_I
    print(i)

    count = (i - 64) - data_bit_len
    print(f'DEBUG - count -> {count}')

    while (count % 8) == 0 and not count == 0:
        count -= 8
        #print(count)
        binary_list.append(format(0, '08b'))

    print(f'DEBUG - binary_list -> {binary_list}')
    print(f'DEBUG - binary_list_len -> {len(binary_list) * 8}')

    """if compare(binary_list):
        print('Nothing wrong here i guess')
    else:
        print('Something is wrong here')"""

    # # # # # # # # # # # # # # # # # #
    # ADD LENGTH AT THE END (64 BIT)  #
    # # # # # # # # # # # # # # # # # #

    data_len = format(CONST_DATA_LEN, '064b')
    k_len_binary_length = len(data_len)

    for i in range(0, k_len_binary_length, 8):
        binary_list.append(data_len[i:i + 8])

    print(binary_list)

"""
    while not (k_len_binary_length % 8) == 0:
        k_len_binary_length += 1

    k_zero_bytes = round((64 - k_len_binary_length) / 8)

    for i in range(0, k_zero_bytes):
        binary_list.append(format(0, '08b'))

    chunks = []
    print(data_len)
    for i in range(len(data_len), 0, -8):
        chunk = data_len[i:i + 8]
        chunks.append(chunk)
    print(chunks)
"""




sha256('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')



