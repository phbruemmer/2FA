
"""
- - - - - - - - - - -
Hashfunction - Encryption
- - - - - - - - - - -

Hashfunction are functions to encrypt data and to securely decrypt data.
The function creates a code (for example 256 Bits long) and encrypts the data with it.
The Code is always the same for the same text but will change if you change something.
"""


def encrypt_data(data):
    data_ascii_list = []
    data_binary_list = []
    print(data)
    for i in data:
        i = ord(i)
        data_ascii_list.append(i)
        data_binary_list.append(bin(i))
        # print(i)
        # print(bin(i))
    print(data_binary_list)


encrypt_data('TestNachricht')

