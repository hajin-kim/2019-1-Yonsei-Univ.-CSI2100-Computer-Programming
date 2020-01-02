def resetValues(L, threshold):
    """
    Reset values
    :param L: The given list(input)
    :param threshold: If a value is bigger than threshold, that value is changed into integer zero(not mutated)
    :return: List L(not mutated)
    """
    Result = []

    for i in L:
        if i > threshold:
            Result.append(0)    # Not cause mutation
        else:
            Result.append(i)

    return Result
    #
    # Test code
    #
    # L=[0,1,2.0,3,4.5]
    # print(L)
    # print(resetValues(L, float(input())))
    # print()
    # for i in L:
    #     print(i, type(i))
    #
