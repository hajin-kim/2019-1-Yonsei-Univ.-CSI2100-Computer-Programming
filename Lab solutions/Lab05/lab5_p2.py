sentence = str(input('Enter a sentence: '))

# Count vowels a e i o u, and capital vowels A E I O U
# from string value sentence.
vowels = sentence.count('a') + \
         sentence.count('e') + \
         sentence.count('i') + \
         sentence.count('o') + \
         sentence.count('u') + \
         sentence.count('A') + \
         sentence.count('E') + \
         sentence.count('I') + \
         sentence.count('O') + \
         sentence.count('U')

# Find whether there is only one vowel in sentence.
if vowels == 1 :
    print('Your sentence contains 1 vowel.')
else :
    print('Your sentence contains', vowels, 'vowels.')
