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
    def rotate_right(value, rotations):
        """
        value : binary string
        rotations : integer
        This function will rotate the binary representation ({rotations} times) to the right.
        """
        rotations = rotations % len(value)
        rot_bits = value[-rotations:]  # Gets the last (-rotation) Bits
        remaining_bits = value[:-rotations]  # Gets the first (rotation) Bits
        rotated_bits = rot_bits + remaining_bits  # Last Bits added in front of the first bits
        return rotated_bits

    def sha_prep():
        binary_list = []

        # Convert Data from ASCII to Binary in 8 Bit chunks
        for i in data:
            binary_data = format(ord(i), '08b')
            binary_list.append(binary_data)

        # Length of the raw data in binary (bitwise)
        CONST_DATA_LEN = len(binary_list) * 8

        # Append single one to the end of the data chunks
        binary_list.append(format(128, '08b'))
        data_binary_len = len(binary_list)

        # Get Data length in bits
        data_bit_len = data_binary_len * 8

        # i equal the size of the current list in bits
        i = 512
        CONST_I = 512

        # While the data_bit_len is smaller than i, add more bits to i
        while data_bit_len + 64 > i:
            i += CONST_I

        count = (i - 64) - data_bit_len

        while (count % 8) == 0 and not count == 0:
            count -= 8
            # print(count)
            binary_list.append(format(0, '08b'))

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

        def block512():
            """
            This function separates the prepared binary list in single 512 Bit blocks.
            """
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
            INCREMENTAL_W0 = 0
            INCREMENTAL_W1 = 1
            INCREMENTAL_W9 = 9
            INCREMENTAL_W14 = 14

            def sigma_zero(w_value):
                """
                This function creates the correct sigma zero binary representation.
                binary:
                    - right rotate 7
                    - right rotate 18
                    - right shift 3
                """
                rr7 = int(rotate_right(w_value, 7).zfill(32), 2)
                rr18 = int(rotate_right(w_value, 18).zfill(32), 2)
                rs3 = int(shift_right(w_value, 3).zfill(32), 2)

                return format((rr7 ^ rr18 ^ rs3), '032b')

            def sigma_one(w_value):
                """
                This function creates the correct sigma one binary representation.
                binary:
                    - right rotate 17
                    - right rotate 19
                    - right shift 10
                """
                rr17 = int(rotate_right(w_value, 17).zfill(32), 2)
                rr19 = int(rotate_right(w_value, 19).zfill(32), 2)
                rs10 = int(shift_right(w_value, 10).zfill(32), 2)

                return format((rr17 ^ rr19 ^ rs10), '032b')

            for i in range(16, 64):
                """
                Loops through w-list and calculates the following values of the list.
                - Stores the current data in the bin_wX variables
                - Calculates sigma_zero and sigma_one.
                - Adds binary values from bin_w0, sigma_zero, bin_w9 and sigma_one
                - Checks if the binary string is longer than 32 bit
                    - if yes, the unnecessary first bits will be removed
                - Appends binary representation on w-list
                - Increments the bin_wX Variables
                """
                bin_w0 = w[INCREMENTAL_W0].zfill(32)
                bin_w1 = w[INCREMENTAL_W1].zfill(32)
                bin_w9 = w[INCREMENTAL_W9].zfill(32)
                bin_w14 = w[INCREMENTAL_W14].zfill(32)

                sig_zero = sigma_zero(bin_w1)
                sig_one = sigma_one(bin_w14)

                next_bin = int(bin_w0, 2) + int(sig_zero, 2) + int(bin_w9, 2) + int(sig_one, 2)
                next_bin = format(next_bin, '032b')
                binary = remove_single_bits(next_bin, 32)
                w.append(binary)

                INCREMENTAL_W0 += 1
                INCREMENTAL_W1 += 1
                INCREMENTAL_W9 += 1
                INCREMENTAL_W14 += 1

        # Function sequence
        block512_data = block512()  # Separates the data into 512 bit chunks
        prep_w(block512_data[0])  # Prepares the w-list -> adds (only) the first 512 bits
        calculate_w_values()  # Calculates the following wX - Values (16..63)
        return w

    def start_hashing():
        """
        calculate final hash
        """

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

            k = []

        # Initial hash value h0..h7
        # First 32 Bits of the fractional parts of the square roots of the first 8 primes.
        h0 = '01101010000010011110011001100111'
        h1 = '10111011011001111010111010000101'
        h2 = '00111100011011101111001101110010'
        h3 = '10100101010011111111010100111010'
        h4 = '01010001000011100101001001111111'
        h5 = '10011011000001010110100010001100'
        h6 = '00011111100000111101100110101011'
        h7 = '01011011111000001100110100011001'

        # Initialize array of constants

        pass

    """binary_prep = sha_prep()
    message_schedule_list = message_schedule(binary_prep)
    print(message_schedule_list)"""


sha256('abc')
