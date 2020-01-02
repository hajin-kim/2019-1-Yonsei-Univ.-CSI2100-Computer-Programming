def copyFiles(f1, f2, f3):
    """
    Copies files f1 and f2 onto file f3.

    If f1, f2 or f3 cannot be opened, -1 is returned.
    Otherwise, the copy operation is performed and 0 is returned.
    :param f1: 'in1.txt'
    :param f2: 'in2.txt'
    :param f3: 'out.txt'
    :return: 0 when performed well, -1 when error occurred
    """
    try:
        # Open file
        file_a = open(f1, 'r')
        file_b = open(f2, 'r')
        file_out = open(f3, 'w')
        add_a = file_a.readline()
        add_b = file_b.readline()
    except OSError:
        return -1

    # About file a
    while add_a != '':
        file_out.write(add_a)
        add_a = file_a.readline()

    file_a.close()

    # About file b
    while add_b != '':
        file_out.write(add_b)
        add_b = file_b.readline()

    file_b.close()

    # Close file output
    file_out.close()
    return 0

    # Test code about return
    # print('return is executed')

    #
    # Test code
    #
    # directory_in1 = 'lab11_p3 output test\\in1.txt'
    # directory_in2 = 'lab11_p3 output test\\in2.txt'
    # directory_out = 'lab11_p3 output test\\out.txt'
    # print('0 : the copy operation is performed and no error')
    # print('-1 : file cannot be opened.')
    # print(copyFiles(directory_in1, directory_in2, directory_out))
