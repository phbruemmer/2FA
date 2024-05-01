import string


def check_password(pw):
    def check_pw():
        check_lowercase = False
        check_uppercase = False
        check_digits = False
        check_punctuation = False

        for i in pw:
            if i in string.ascii_lowercase:
                check_lowercase = True
            if i in string.ascii_uppercase:
                check_uppercase = True
            if i in string.digits:
                check_digits = True
            if i in string.punctuation:
                check_punctuation = True
            if check_digits and check_punctuation and check_uppercase and check_lowercase:
                return True

    print(pw)
    if len(pw) >= 5 and check_pw():
        return True
    else:
        return False
