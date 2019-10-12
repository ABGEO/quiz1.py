def vowels_and_consonants():
    string = input('Enter the string: ')

    length = len(string)
    vowels_count = 0
    consonants_count = 0
    string_without_vowels = ''

    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']

    for char in string:
        if char.upper() in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
            string_without_vowels += char

    return length, vowels_count, consonants_count, string_without_vowels
