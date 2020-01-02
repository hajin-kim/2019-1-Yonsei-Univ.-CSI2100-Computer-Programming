inp = int(input('Enter an integer: '))

i = inp

# The loop will be executed inp times.
# Once loop executed will reduce i so that it can break when i is 0.
while i :
    space = inp - i
    width = 2*i - 1

    # Enter blanks, one blank per each print statements.
    while space :
        print(end=' ')
        space -= 1

    # Enter stars, one star per each print statements.
    while width :
        print(end='*')
        width -= 1

    # Go to next sentence.
    print()
    i -= 1
