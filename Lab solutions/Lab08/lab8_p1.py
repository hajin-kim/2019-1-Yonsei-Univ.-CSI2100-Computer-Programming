def resetValuesInPlace(L, threshold):
    """
    Reset values
    :param L: The given list(input)
    :param threshold: If a value is bigger than threshold, that value is changed into integer zero
    :return: List L(mutated)
    """
    for i in range(len(L)):
        if L[i] > threshold:
            L[i] = 0    # Cause mutation

    return L
    #
    # Test code
    #
    # L=[0,1,2.0,3,4.5]
    # print(L)
    # print(resetValuesInPlace(L, float(input())))
    # print()
    # for i in L:
    #     print(i, type(i))
    #
