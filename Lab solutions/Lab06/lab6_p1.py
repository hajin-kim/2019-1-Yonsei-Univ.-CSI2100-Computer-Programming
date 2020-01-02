name = str(input('Enter a first and last name: '))
i = 0

# Find initial of the first name
flag = True
while flag:
    if name[i] != ' ':
        name_first = name[i]
        flag = False
    i += 1

# Find the start of the blank(s)
flag = True
while flag:
    if name[i] == ' ':
        flag = False
    i += 1

# Find the start of the family name
flag = True
while flag:
    if name[i] != ' ':
        name_family_start = i
        flag = False
    i += 1

# Find the end of the family name
# Watch out for the following blank(s) or no one
flag = True
while len(name) > i and flag:
    # if len(name) >= i+3:
    #     if name[i] == ' ':
    #         name_family_end = i - 1
    #         flag = False
    # elif len(name) == i+2:
    #     name_family_end = i - 1
    #     flag = False
    if name[i] == ' ':
        i -= 1
        flag = False
    i += 1
    # else : name_family = name[name_family_start : ]

name_family = name[name_family_start : i]

print(name_family+', '+name_first+'.')

# a = name[name.index(' ') -1 : ]
# print(name[0]+',', a)
