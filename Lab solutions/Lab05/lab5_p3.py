# Declare the val 'L' as a blank list
L = []
# Use Boolean flag
i = True

while i :
    inp = int(input('Enter an integer: '))

# Append L by following if-else statements
    if inp > 100 :
        L.append('over')
    elif inp == 0 :
        # Boolean flag down
        i = False
    else :
        L.append(inp)

print(L)
