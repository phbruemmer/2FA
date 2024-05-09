
"""
- - - - - - - - - - -
Hashfunction - Encryption
- - - - - - - - - - -

Hashfunction are functions to encrypt data and to securely decrypt data.
The function creates a code (for example 256 Bits long) and encrypts the data with it.
The Code is always the same for the same text but will change if you change something.
"""


DEBUG = False



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
    bin_to_compare = get_bin(""" """)
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
    def sha_prep():
        print(data)
        binary_list = []

        # Convert Data from ASCII to Binary in 8 Bit chunks
        for i in data:
            binary_data = format(ord(i), '08b')
            binary_list.append(binary_data)
            if DEBUG:
                print(binary_data)

        # Length of the raw data in binary (bitwise)
        CONST_DATA_LEN = len(binary_list) * 8

        # Append single one to the end of the data chunks
        binary_list.append(format(128, '08b'))
        data_binary_len = len(binary_list)

        if DEBUG:
            print(f'DEBUG - data_binary_len -> {data_binary_len}')
        # Get Data length in bits
        data_bit_len = data_binary_len * 8
        if DEBUG:
            print(f'DEBUG - data_bit_len -> {data_bit_len}')

        # i equal the size of the current list in bits
        i = 512
        CONST_I = 512

        # While the data_bit_len is smaller than i, add more bits to i

        while data_bit_len + 64 > i:
            i += CONST_I

        count = (i - 64) - data_bit_len
        if DEBUG:
            print(f'DEBUG - count -> {count}')

        while (count % 8) == 0 and not count == 0:
            count -= 8
            # print(count)
            binary_list.append(format(0, '08b'))

        if DEBUG:
            print(f'DEBUG - binary_list -> {binary_list}')
            print(f'DEBUG - binary_list_len -> {len(binary_list) * 8}')

        # # # # # # # # # # # # # # # # # #
        # ADD LENGTH AT THE END (64 BIT)  #
        # # # # # # # # # # # # # # # # # #

        data_len = format(CONST_DATA_LEN, '064b')
        k_len_binary_length = len(data_len)

        for i in range(0, k_len_binary_length, 8):
            binary_list.append(data_len[i:i + 8])
        print(binary_list)
        return binary_list

    def message_schedule(msg_data_block):
        w = []  # Array w[0..63] of 32-bit words

        def rotate_right(rotations):
            pass

        def shift_right(shifts):
            pass

        def block512():
            """
            This function separates the prepared binary list in single 512 Bit blocks.
            """
            print(len(msg_data_block))
            final_block = []

            for y in range(0, len(msg_data_block), 64):
                final_block.append(msg_data_block[y:y + 64])
            return final_block

        def prep_w(_512bit_chunk):
            """
            This function inserts the first 512 bits into the w0..63 Message Schedule list.
            """
            temp_binary_str = ''
            k = 0
            for i in range(0, len(_512bit_chunk)):
                temp_binary_str += _512bit_chunk[i]
                k += 1
                if (k % 4) == 0 and not k == 0:
                    k = 0
                    w.append(temp_binary_str)
                    temp_binary_str = ''

        def calculate_w_values():
            ITERATABLE_W0 = 0
            ITERATABLE_W1 = 1
            ITERATABLE_W9 = 9
            ITERATABLE_W14 = 14

            def sigma_zero():
                pass

            def sigma_one():
                pass
            print(w)

        block512_data = block512()
        prep_w(block512_data[0])
        calculate_w_values()

    binary_prep = sha_prep()
    message_schedule(binary_prep)


sha256('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
