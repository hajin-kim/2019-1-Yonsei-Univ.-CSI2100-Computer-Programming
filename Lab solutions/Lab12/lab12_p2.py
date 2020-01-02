def moderateDays(mydict):
    """
    Returns a list [...] of the days for which the average
    temperature was between 70 and 79 degrees.
    :param mydict:
    :return:
    """
    result = []
    for keys in mydict:
        if 70 <= mydict[keys] <= 79:
            result.append(keys)

    return result

    # # Test code
    #
    # mydict = {'Sun':69, 'Mon':70, 'Tue':71,
    #           'Wed':75, 'Thu':78,'Fri':79, 'Sat':80}
    #
    # print(moderateDays(mydict))
