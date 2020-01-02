inp = input('Enter the first 12 digits of an EAN: ')

t = int(inp)
a = t % 10

t = t // 10
b = t % 10

t = t // 10
c = t % 10

t = t // 10
d = t % 10

t = t // 10
e = t % 10

t = t // 10
f = t % 10

t = t // 10
g = t % 10

t = t // 10
h = t % 10

t = t // 10
i = t % 10

t = t // 10
j = t % 10

t = t // 10
k = t % 10

t = t // 10
l = t % 10

step1 = a + c + e + g + i + k
step2 = b + d + f + h + j + l
step3_1 = step1 * 3
step3_2 = step2 + step3_1
step4 = step3_2 - 1
step5 = step4 % 10
step6 = 9 - step5

print('Check digit:', step6)

# Feedback : -1 wrong coding style : missing comment
