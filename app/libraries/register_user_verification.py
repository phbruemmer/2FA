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

"""
- save link in db (username, custom_link)
- move user credentials from temp to main
    - In case of no verification:
        - delete user in temp after 20 min
    - In case of no received message (resend email on btn-click)
        - delete custom link from db and create new one
"""