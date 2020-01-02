word = []
enter_word = str(input('Enter a word (q to quit): '))

# Get list of word
while enter_word != 'q':
    word.append(enter_word)
    enter_word = str(input('Enter a word (q to quit): '))

# Sort first
word.sort()
i = 0

# Chosen while because the len(word) have to be changed when words are deleted
while i < len(word):
    flag = False

    # To compare between large and small, convert the initial and looking character to UTF-8
    initial = ord(word[i][0])
    for j in range(1, len(word[i])):
        looking = ord(word[i][j])

        # If the character is completely equal, even whether large or small
        if initial == looking:
            flag = True
        # 'a' <= initial <= 'z' then diminish 32 to make it large and compare
        elif initial >= 97 and initial <= 122:
            if initial - 32 == looking:
                flag = True
        # 'A' <= initial <= 'Z' then augment 32 to make it small and compare
        elif initial >= 65 and initial <= 90:
            if initial + 32 == looking:
                flag = True

    # If flag is still down, delete the word,
    # and do NOT augment i so that the remaining values of list can be shifted to left one
    if flag: i += 1
    else: del word[i]

print(word)
