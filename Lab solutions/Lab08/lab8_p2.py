def removeValuesInPlace(L, threshold):
    """
    Remove values
    :param L: The given list(input)
    :param threshold: If a value is bigger than threshold, that value is removed
    :return: List L(mutated)
    """
    i = 0

    while i < len(L):
        if L[i] > threshold:
            del L[i]    # Cause mutation
        else:
            i += 1

    return L
    #
    # Test code
    #
    # L=[0,1,2.0,3,4.5]
    # print(L)
    # print(removeValuesInPlace(L, float(input())))
    # print()
    # for i in L:
    #     print(i, type(i))
    #
