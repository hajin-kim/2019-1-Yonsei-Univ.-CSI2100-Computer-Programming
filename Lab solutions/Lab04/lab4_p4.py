a = 1
while a <= 100 :
    print(format(a, '>3'), end='')
    a += 1
    if a % 10 == 1:
        print('')
