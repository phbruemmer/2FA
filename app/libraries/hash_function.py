from statics import static_hash_values as shv
import logical_operators as lo
import hash_calculations as hc

"""
- - - - - - - - - - -
Hashfunction - Encryption
- - - - - - - - - - -
A hash function transforms input data of any size into a fixed-size string of characters, called a hash value. 
It is used in data structures like hash tables for efficient retrieval and in cybersecurity to ensure data integrity. 
Cryptographic hash functions, like SHA-256, are designed to be secure, making it hard 
to find two inputs that produce the same hash. Hash functions are crucial for efficient data management 
and robust security.
"""


def sha256(data):
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

                sig_zero = hc.sigma_zero(bin_w1)
                sig_one = hc.sigma_one(bin_w14)

                next_bin = int(bin_w0, 2) + int(sig_zero, 2) + int(bin_w9, 2) + int(sig_one, 2)
                next_bin = format(next_bin, '032b')
                binary = hc.remove_single_bits(next_bin, 32)
                w.append(binary)

                INCREMENTAL_W0 += 1
                INCREMENTAL_W1 += 1
                INCREMENTAL_W9 += 1
                INCREMENTAL_W14 += 1

        # Function sequence
        block512_data = block512()  # Separates the data into 512 bit chunks
        prep_w(block512_data[0])    # Prepares the w-list -> adds (only) the first 512 bits
        calculate_w_values()        # Calculates the following wX - Values (16..63)
        return w

    def start_hashing(w):
        """
        w: w_list
        calculate final hash
        """

        # Initial array of h-constants
        # First 32 Bits of the fractional parts of the square roots of the first 8 primes. (2..19)
        h = shv.create_h_constants()

        # Working Variables
        a_ = h[0]
        b_ = h[1]
        c_ = h[2]
        d_ = h[3]
        e_ = h[4]
        f_ = h[5]
        g_ = h[6]
        h_ = h[7]

        # Initial array of k-constants
        # First 32 Bits of the fractional parts of the cube roots of the first 64 primes. (2..311)
        k = shv.create_k_constants()

        for i in range(0, len(k)):
            # Create Temps
            # Temp1 = h + sigma1 + Choice + k[n] + w[n]

            t1_1 = lo.add_binary(h_, hc.sigma_one(e_))
            t1_2 = lo.add_binary(k[i], w[i])
            t1_3 = lo.add_binary(t1_1, t1_2)

            Temp1 = lo.add_binary(t1_3, hc.choice(e_, f_, g_))
            Temp1 = hc.remove_single_bits(Temp1, 32)

            Temp2 = lo.add_binary(hc.sigma_zero(a_), hc.majority(a_, b_, c_))
            Temp2 = hc.remove_single_bits(Temp2, 32)

            # Update working Variables
            h_ = g_
            g_ = f_
            f_ = e_
            e_ = hc.remove_single_bits(lo.add_binary(d_, Temp1), 32)
            d_ = c_
            c_ = b_
            b_ = a_
            a_ = hc.remove_single_bits(lo.add_binary(Temp1, Temp2), 32)

        h0 = hc.remove_single_bits(lo.add_binary(a_, (h[0])), 32)
        h1 = hc.remove_single_bits(lo.add_binary(b_, h[1]), 32)
        h2 = hc.remove_single_bits(lo.add_binary(c_, h[2]), 32)
        h3 = hc.remove_single_bits(lo.add_binary(d_, h[3]), 32)
        h4 = hc.remove_single_bits(lo.add_binary(e_, h[4]), 32)
        h5 = hc.remove_single_bits(lo.add_binary(f_, h[5]), 32)
        h6 = hc.remove_single_bits(lo.add_binary(g_, h[6]), 32)
        h7 = hc.remove_single_bits(lo.add_binary(h_, h[7]), 32)

        result = hex(int(h0, 2))[2:]
        result += hex(int(h1, 2))[2:]
        result += hex(int(h2, 2))[2:]
        result += hex(int(h3, 2))[2:]
        result += hex(int(h4, 2))[2:]
        result += hex(int(h5, 2))[2:]
        result += hex(int(h6, 2))[2:]
        result += hex(int(h7, 2))[2:]
        return result

    binary_prep = sha_prep()
    message_schedule_list = message_schedule(binary_prep)
    final_hash = start_hashing(message_schedule_list)
    return final_hash


if __name__ == "__main__":
    print(sha256('abc'))

# ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
