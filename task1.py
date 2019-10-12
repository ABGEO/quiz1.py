import random


def random_action():
    number = random.randrange(2)
    string = input('Enter the string: ')

    if 1 == number:
        return_value = 'The string without "a": '
        for char in string:
            if char not in ['a', 'A']:
                return_value += char
    else:
        a_pos = string.find('a')

        if -1 == a_pos:
            return_value = 'We don\' have "a" in string'
        else:
            return_value = 'We have first "a" at position ' + str(a_pos)

    return return_value, len(string)
