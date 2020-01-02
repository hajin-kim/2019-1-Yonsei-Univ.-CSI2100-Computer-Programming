state = ('GS1 prefix', 'Group identifier', 'Publisher code', 'Item number', 'Check digit')

isbn = str(input('Enter an ISBN: '))

a = isbn.split('-')

# Do 5 times. i is in [0, 4]
for i in range(5):
    print(format(a[i],'.<20')+state[i])
