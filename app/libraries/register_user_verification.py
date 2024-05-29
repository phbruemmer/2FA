"""
           Verify:
            - Send E-Mail with verify link
            - check if verify link was opened

            verify-link-structure:
                '.../verify/username/random_generated_code'
"""

import random
import string


def create_custom_url(username):
    def create_random():
        char = ''
        num = random.randint(0, 1)
        if num == 0:
            char = string.ascii_letters[random.randint(0, len(string.ascii_letters) - 1)]
        elif num == 1:
            char = string.digits[random.randint(0, len(string.digits) - 1)]
        return char

    def create_custom_str():
        final_str = ""
        for i in range(random.randint(12, 18)):
            final_str += create_random()
        return final_str

    custom_url = '../verify/'
    custom_str = create_custom_str()

    custom_url += username + '/' + custom_str + '/'

    return [custom_url, custom_str]


def create_recovery_code(user_id):
    user_id = str(user_id)
    def create_random():
        char = ''
        num = random.randint(0, 1)
        if num == 0:
            char = string.ascii_letters[random.randint(0, len(string.ascii_letters) - 1)]
        elif num == 1:
            char = string.digits[random.randint(0, len(string.digits) - 1)]
        return char

    def create_custom_str():
        final_str = ""
        for i in range(random.randint(24, 32)):
            final_str += create_random()
        return final_str

    custom_url = '../recovery/'
    custom_str = create_custom_str()

    custom_url += user_id + '/' + custom_str + '/'

    return [custom_url, custom_str]


def create_code():
    code = ''
    for i in range(0, 6):
        code += string.digits[random.randint(0, 9)]
    return code


if __name__ == "__main__":
    print(create_recovery_code(12353425))
