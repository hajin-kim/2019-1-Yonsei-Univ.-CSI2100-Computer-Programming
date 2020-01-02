# No stack nor any other auxiliary data-structure is needed

print('This program can determine if a given string is a palindrome\n')
print('(Enter return to exit)')

chars = input('Enter string to check: ')
chars_length = len(chars)

# If input is NULL, terminate
while chars_length:

    # About a one letter word
    if chars_length == 1:
        print('A one letter word is by definition a palindrome\n')

    else:
        is_palindrome = True
        for i in range(0, chars_length//2):
            if chars[i] != chars[chars_length-i-1]:
                is_palindrome = False

        # Print the result
        if is_palindrome:
            print(chars, 'is a palindrome\n')
        else:
            print(chars, 'is NOT a palindrome\n')

    # Get again
    chars = input('Enter string to check: ')
    chars_length = len(chars)

    # Run until program is terminated(by NULL)
