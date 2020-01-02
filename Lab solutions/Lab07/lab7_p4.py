def evalPolynomial(x):
    """
    Calculates the function
    :param x: The input value
    :return: The result of calculating
    """
    return x ** 5 * 3 + x ** 4 * 2 - x ** 3 * 5 - x ** 2 + x * 7 - 6

inp = int(input('Enter a value for x: '))

# Print the result using function
print('Polynomial for x=', inp, ': ',evalPolynomial(inp), sep='')
