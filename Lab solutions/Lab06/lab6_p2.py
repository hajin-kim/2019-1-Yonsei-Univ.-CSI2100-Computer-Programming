inp = str(input('Enter a fraction: '))

no_space = ''

# Remove all blanks by storing on a new variable
for ch in inp:
    if ch != ' ':
        no_space += ch

# Find the index of '/'
slash_index = no_space.index('/')

# Slice the input that blanks are removed, by found '/'
numerator = int(no_space[:slash_index])
denominator = int(no_space[slash_index+1:])

# Precedence : if the fraction can be changed into the shape of 'x/1'
if numerator % denominator == 0:
    print('In lowest terms:', int(numerator/denominator))
else:
    # Declare max value and min one
    if numerator > denominator:
        maxi = numerator
        mini = denominator
    else:
        maxi = denominator
        mini = numerator

    # Use Euclid's Algorithm to get GCD on value 'mini'
    remainder = maxi % mini
    while remainder:
        maxi = mini
        mini = remainder
        remainder = maxi % mini

    # Print as given form
    print('In lowest terms: ', int(numerator/mini), '/', int(denominator/mini), sep='')
