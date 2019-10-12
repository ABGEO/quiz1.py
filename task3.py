def substring():
    string = input('Enter the string: ')
    string = string.strip()

    length = string.count('ad')
    space_pos = string.find(' ')

    return str(length), string[0] + ' ' + string[space_pos+1:]
