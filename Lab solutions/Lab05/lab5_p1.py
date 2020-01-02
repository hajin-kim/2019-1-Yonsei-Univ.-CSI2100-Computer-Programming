inp = float(input('Enter a number: '))

lar = 0

# Get until 0 is gotten.
# If the first input isn't 0 or less, then lar must be renewed.
while inp > 0 :
    if inp > lar :
        lar = inp
    inp = float(input('Enter a number: '))

# If the first input is 0 or less, then lar is 0.
# Because the loop statement wouldn't be executed.
if lar == 0 :
    print('No positive number was entered')
else :
    print('The largest number entered was', format(lar, '.2f'))
