def addDailyTemp(mydict, day, temperature):
    """
    Add key 'day' and value 'temperature' to the dictionary 'mydict',
    only if key 'day' does not already exist in the dictionary.
    The resulting dictionary is returned.
    :param mydict:
    :param day:
    :param temperature:
    :return:
    """
    if day not in mydict:
        mydict[day] = temperature

    return mydict

    # # Test code
    #
    # mydict = {}
    #
    # print(addDailyTemp(mydict, 'Monday', 1))
    # print(addDailyTemp(mydict, 'Mon', 1))
    # print(addDailyTemp(mydict, 'Montag', 1))
    # print(addDailyTemp(mydict, 1, 1))
    # print(addDailyTemp(mydict, 'Monday', 2))
    # print(addDailyTemp(mydict, 'Mon', 2))
    # print(addDailyTemp(mydict, 'Montag', 2))
    # print(addDailyTemp(mydict, 1, 2))
