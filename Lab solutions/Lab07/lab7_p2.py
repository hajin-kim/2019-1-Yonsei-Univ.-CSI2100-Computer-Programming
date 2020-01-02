def ordered3(num1, num2, num3):
    """
    Check in order
    :param num1: int
    :param num2: int
    :param num3: int
    :return: If it is in order, Boolean rue. Else, Boolean False
    """
    # Use this inspector statement
    # print(ordered3(int(input()),int(input()),int(input())))
    if num1 <= num2 and num2 <= num3:
        return True
    else:
        return False
