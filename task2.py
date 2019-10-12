def iteration_sum(a, b):
    if a == b:
        return b
    else:
        return a + iteration_sum(a + 1, b)


def b_in_string():
    string = input('Enter the string: ')

    if string.count('b') > 5:
        return 'ბევრია'

    while string.count('b') < 5:
        string += input('"b" not Enough! enter it! ')

    sum1_20 = iteration_sum(1, 20)
    return 'Iteration sum form 1 to 20 is: ' + str(sum1_20)
