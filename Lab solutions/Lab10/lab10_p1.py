def countLetters(line):
    """
    Count all letter characters in string ``line'' and write the
    result to file ``answer.txt''.

    The number of letter characters must be written to the file:
    countLetters('abA1 23') -> writes 3
    countLetters('!') -> writes 0
    :param line:input characters
    :return:none
    """
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # ch.isalpha()
    counter = 0

    for i in line:
        if i in characters:
            counter += 1

    answer_textfile = open('anwser.txt', 'w')
    answer_textfile.write(str(counter)+'\n')
    answer_textfile.close()

    # myfile.write(str(22) + '\n')

    #
    # Test code
    #
    # countLetters(str(input('test input: ')))
    #
