digit3 = int(input('Enter leftmost digit: '))
digit2 = int(input('Enter the next digit: '))
digit1 = int(input('Enter the next digit: '))
digit0 = int(input('Enter the next digit: '))

result_value = digit0 * (2 ** 0) + digit1 * (2 ** 1) + digit2 * (2 ** 2) + digit3 * (2 ** 3)

print('The value is', result_value)
