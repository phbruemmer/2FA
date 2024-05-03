
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
        binary_list.append(bin(ord(i)))
    # Get bitwise length of data input
    data_binary_len = len(binary_list) * 8
    # calculate zeros to append
    k = 896 - (data_binary_len + 1)


    print(binary_list)

sha256('TestNachricht')

