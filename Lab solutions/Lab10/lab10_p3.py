def countAllLetters(line):
    """
    Counts letters in 'line' and returns result list. If the line
    does not contain any letter, returns an empty list.

    Note 1: the list of letters must be sorted alphabetically.
            (This is a requirement in addition to the textbook problem.)
    Note 2: your letters in the result-list must be stored in lower-case.
    :param line: given string
    :return: list made
    """

    line_sorted = line.lower()

    result = []

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        counter = line_sorted.count(letter)
        if counter > 0:
            result.append((letter, counter))

    # print(result)

    return result

    #
    # Test code
    #
    # print(countAllLetters('This is the shortest LINE...,   '))
    # print(countAllLetters('This is a short line'))
    #

    #
    # [('e', 3), ('h', 3), ('i', 3), ('l', 1), ('n', 1),
    # ('o', 1), ('r', 1), ('s', 4), ('t', 4)]
    #
    # [('t', 2), ('h', 2), ('i', 3), ('s', 3), ('a', 1),
    # ('o', 1), ('r', 1), ('l', 1), ('n', 1), ('e', 1)]
    #
