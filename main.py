import task1
import task2
import task3
import task4
import task5
import task6


def task1_runner():
    output, length = task1.random_action()
    print('Output is: ' + output + '\nLength in: ' + str(length))


def task2_runner():
    task2_return = task2.b_in_string()
    print(task2_return)


def task3_runner():
    sub_count, task3_return = task3.substring()
    print('Count of "ad" in string: ' + str(sub_count))
    print('The first letter and string after first word: ' + task3_return)


def task4_runner():
    length, vowels_count, consonants_count, string_without_vowels = task4.vowels_and_consonants()
    print('Letters in string: ' + str(length))
    print('Vowels in string: ' + str(vowels_count))
    print('Consonants in string: ' + str(consonants_count))
    print('String without vowels: ' + string_without_vowels)


def task5_runner():
    string = input('Enter the string: ')
    longest = task5.longest_sub(string)
    print('The longest increasing substring is "' + longest + '"')


def task6_runner():
    string = input('Enter the string: ')
    is_palindrome = task6.is_palindrome(string)

    if is_palindrome:
        print('The string "' + string + '" is palindrome')
    else:
        print('The string "' + string + '" is not palindrome')


if __name__ == '__main__':
    # task 1:
    print('Task 1: \n\n')
    task1_runner()
    print('End of Task 1 \n\n')

    # task 2:
    print('Task 2: \n\n')
    task2_runner()
    print('End of Task 2 \n\n')

    # task 3:
    print('Task 3: \n\n')
    task3_runner()
    print('End of Task 3 \n\n')

    # task 4:
    print('Task 4: \n\n')
    task4_runner()
    print('End of Task 4 \n\n')

    # task 5:
    print('Task 5: \n\n')
    task5_runner()
    print('End of Task 5 \n\n')

    # task 6:
    print('Task 6: \n\n')
    task6_runner()
    print('End of Task 6 \n\n')
