def copyFiles(f1, f2, f3):
    """
    Copies f1 and f2 onto f3.

    The function assumes that files f1 and f2 can be opened, and that
    no error occurs in writing file f3.
    Therefore, the function will always return 0.
    (Error handling with file I/O will be part of next week's lecture.)
    :param f1: 'in1.txt'
    :param f2: 'in2.txt'
    :param f3: 'out.txt'
    :return: none
    """
    # Make file output
    file_out = open(f3, 'w')

    # About file a

    file_a = open(f1, 'r')

    add = file_a.readline()
    while add != '':
        file_out.write(add)
        add = file_a.readline()

    file_a.close()

    # About file b

    file_b = open(f2, 'r')

    add = file_b.readline()
    while add != '':
        file_out.write(add)
        add = file_b.readline()

    file_b.close()

    # Close file output
    file_out.close()

    #
    # Test code
    #
    # copyFiles('p2 in1.txt', 'p2 in2.txt', 'p2 out.txt')
    #
