def point_printer(length):
    """
    Print point(s)
    :param length: Length of the digit(s)
    :return: None
    """
    print(end='.'*(20-length))

state = ('GS1 prefix', 'Group identifier', 'Publisher code', 'Item number', 'Check digit')

isbn = str(input('Enter an ISBN: '))

a = isbn.split('-')

# Do 5 times. i is in [0, 4]
for i in range(5):

    print(end=a[i])

    # Print point(s)
    point_printer(len(a[i]))

    # Print identifier
    print(state[i])
