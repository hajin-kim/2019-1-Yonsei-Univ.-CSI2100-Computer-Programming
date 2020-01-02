inp = int(input('Enter a number: '))
a = inp
digit = 1
while a >= 10 :
    a = a // 10
    digit += 1
if digit == 1 :
    print('The number', inp, 'contains', digit, 'digit')
else :
    print('The number', inp, 'contains', digit, 'digits')
