import random


def getFile(file):
    """
    Return all characters as string from file
    :param file: opened file object
    :return: string
    """
    result = ''

    for line in file:
        result += line

    return result


def e_makeEncryptKey(chars):
    """
    Able to call itself when the last value is overlapped
    :param chars: characters A to Z, a to z, blank, 0 to 9
    :return: key list
    """
    chars_list = list(chars)
    result = []

    length = len(chars_list)
    for i in range(0, length - 1):
        random_index = random.randint(0, length - 1 - i)
        key = chars_list[random_index]
        # print(random_index)
        while key == chars[i]:
            random_index = random.randint(0, length - 1 - i)
            key = chars_list[random_index]

        result += key

        del chars_list[random_index]

        # print(key_encrypted)
        # print(key_original)

    if chars_list[0] == chars[-1]:
        return e_makeEncryptKey(chars)
    else:
        return result + [chars_list[0]]


def replaceCharacters(string, key):
    """
    Change characters from dictionary key into dictionary value
    The dictionary is initialized along e or d mode
    :param string: all characters from file
    :param key: dictionary initialized along e or d mode
    :return: replaced string
    """
    result = ''

    for ch in string:
        if ch in key:
            result += key[ch]
        else:
            result += ch

    return result


""" Main domain """

# Get input file name
file = input('Enter a filename: ')
file_name = file[:-4]
file_extension = file[-3:]
# print(file_name)
# print(file_extension)

# Init mode e or d
mode_encrypt = False
mode_decrypt = False

# Key dictionary replacer
key = {}

if file_extension == 'txt':
    mode_encrypt = True
elif file_extension == 'enc':
    mode_decrypt = True

if mode_encrypt:
    # Init key changer strings
    key_original = ''
    for ch in range(ord('A'), ord('Z')+1):
        key_original += chr(ch)
    for ch in range(ord('a'), ord('z')+1):
        key_original += chr(ch)
    key_original += ' '
    for ch in range(ord('0'), ord('9')+1):
        key_original += chr(ch)

    key_encrypted = e_makeEncryptKey(key_original)

    # # Test code
    # # Find overlapped value
    #
    # while True:
    #     key_encrypted = encrypt(key_original)
    #     tester = list(key_original)
    #     print(tester)
    #     for i in range(0, len(key_encrypted)):
    #         if key_encrypted[i] == tester[i]:
    #             while True:
    #                 print()
    #     print(key_encrypted)
    #     key_encrypted.sort()
    #     # print(key_encrypted)
    #     for i in range(0, len(key_encrypted)):
    #         if key_encrypted[i] != tester[i]:
    #             while True:
    #                 print()
    #

    # Make key
    for i in range(0, len(key_original)):
        key[key_original[i]] = key_encrypted[i]

    # Make key file
    file_key_encrypt = open(file_name+'.key', 'w')

    for i in range(0, len(key_original)):
        file_key_encrypt.write(key_original[i]+','+key_encrypted[i]+'\n')

    file_key_encrypt.close()

    file_output = open(file_name+'.enc', 'w')

elif mode_decrypt:
    # Get key file
    file_key_decrypt = open(file_name+'.key', 'r')

    # Make key
    for line in file_key_decrypt:
        key[line[2]] = line[0]

    file_output = open(file_name+'.txt', 'w')

# Get texts from input file
file_input = open(file, 'r')
all_characters = getFile(file_input)
file_input.close()

# Get replaced result
text_replaced = replaceCharacters(all_characters, key)

# Make output file
file_output.write(text_replaced)
file_output.close()
# print(text_replaced)
