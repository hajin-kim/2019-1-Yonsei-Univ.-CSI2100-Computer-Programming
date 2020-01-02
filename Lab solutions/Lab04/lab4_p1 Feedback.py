inp_income = int(input('Enter the taxable income in USD: '))

if inp_income < 750 :
    tax = inp_income * 0.01
elif inp_income < 2250 :
    tax = (inp_income - 750) * 0.02 + 7.5
elif inp_income < 3750 :
    tax = (inp_income - 2250) * 0.03 + 37.5
elif inp_income < 5250 :
    tax = (inp_income - 3750) * 0.04 + 82.5
elif inp_income < 7000 :
    tax = (inp_income - 5250) * 0.05 + 142.5    # Feedback : missing "* 0.05"
else :
    tax = (inp_income - 7000) * 0.06 + 230

print('Tax due:', format(tax, '.2f'), 'USD')

# Feedback : -1 wrong coding style : missing comment
# Feedback : -1(5%) evaluating error on one test case : missing "* 0.05"
