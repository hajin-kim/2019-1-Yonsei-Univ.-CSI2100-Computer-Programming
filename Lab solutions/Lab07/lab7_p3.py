def modCount(n, m):
    """
    Count the number of mod
    :param n: The interval
    :param m: m <= n
    :return: The number of mod
    """
    # Use this inspector statement
    # print(modCount(int(input()),int(input())))
    counter = 0
    for i in range(1,n+1):
        if i % m == 0:
            counter += 1
    return counter
