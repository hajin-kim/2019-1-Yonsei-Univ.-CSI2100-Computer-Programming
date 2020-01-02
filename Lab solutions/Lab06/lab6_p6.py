L = int(input('Enter the limit L: '))

# Because L is 0 or greater integer that 0, we can use it as a Boolean flag
while L:
    # Maybe rounding error occurs
    terms = float(1)
    for i in range(2, L+1):
        terms += 1 / i
    print('Sum of the initial', L, 'term(s):', format(terms, '.6f'))
    L = int(input('Enter the limit L: '))
