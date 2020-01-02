first_name = str(input('Enter a name (q to quit): '))

# Declare the val 'L' as a blank list
L = []

while first_name != 'q' :
    L.append(first_name)
    first_name = str(input('Enter a name (q to quit): '))
# The last letter 'q' doesn't included in list

length = len(L)
cnt = 0
i = 0

# Find both 'a' and 'A' from L[0] to L[length - 1]
while i < length :
    cnt += L[i].count('a') + L[i].count('A')
    i += 1

print('Appearance of letter \'a\':', cnt)
