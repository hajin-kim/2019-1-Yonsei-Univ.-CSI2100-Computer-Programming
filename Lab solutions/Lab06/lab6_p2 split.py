inp = str(input('Enter a fraction: '))

# Make an offset between the numerator and the denominator
temp = list(inp.split('/'))

# Remove all blanks with split
temp_numerator = temp[0].split()
temp_denominator = temp[1].split()

# Convert what is saved as list to integer
numerator = int(temp_numerator[0])
denominator = int(temp_denominator[0])

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
