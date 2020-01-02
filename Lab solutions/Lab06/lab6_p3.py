# Password Encryption/Decryption Program

# init
import sys # Importing system function is added

password_out = ''
case_changer = ord('a') - ord('A')
encryption_key = (('a', 'm'), ('b', 'h'), ('c', 't'), ('d', 'f'), ('e', 'g'),
                  ('f', 'k'), ('g', 'b'), ('h', 'p'), ('i', 'j'), ('j', 'w'), ('k', 'e'), ('l', 'r'),
                  ('m', 'q'), ('n', 's'), ('o', 'l'), ('p', 'n'), ('q', 'i'), ('r', 'u'), ('s', 'o'),
                  ('t', 'x'), ('u', 'z'), ('v', 'y'), ('w', 'v'), ('x', 'd'), ('y', 'c'), ('z', 'a'),
                  ('#', '!'), ('@', '('), ('%', ')')) # Non-alphabetic characters are added

encrypting = True

# get password
password_in = str(input('Enter password: '))



# Following codes are newly added

# Use Boolean flag. When this program detects either alphabet, digit or non, each flag off
switch_alpha = True
switch_digit = True
switch_non = True
# Set the allowed characters
allowed = list(range(ord('a'), ord('z')+1)) + list(range(ord('A'), ord('Z')+1)) + \
          list(range(ord('0'), ord('9')+1)) + [ord('#'), ord('@'), ord('%')]

for i in password_in:
    # If not allowed character, then program terminates
    if ord(i) not in allowed:
        print('Invalid password!')
        sys.exit()
    else:
        # Following if statements are not able to be simultaneous, so if-elif
        if ('a' <= i and i <= 'z') \
                or ('A' <= i and i <= 'Z'):
            switch_alpha = False
        elif '0' <= i and i <= '9':
            switch_digit = False
        elif ((i == '#') or (i == '@')) or (i == '%'):
            switch_non = False

# If any flag is up, terminate this program
if (switch_alpha or switch_non) or switch_digit:
    print('Invalid password!')
    sys.exit()

# Upper codes are newly added



# perform encryption / decryption
if encrypting:
    from_index = 0
    to_index = 1
else:
    from_index = 1
    to_index = 0

case_changer = ord('a') - ord('A')

for ch in password_in:
    letter_found = False

    for t in encryption_key:
        if ('a' <= ch and ch <= 'z') and ch == t[from_index]:
            password_out = password_out + t[to_index]
            letter_found = True
        elif ('A' <= ch and ch <= 'Z') and chr(ord(ch) + 32) == t[from_index]:
            password_out = password_out + chr(ord(t[to_index]) - case_changer)
            letter_found = True

        # Following 9 codes are newly added
        elif ch == '#' and ch == t[from_index]:
            password_out = password_out + t[to_index]
            letter_found = True
        elif ch == '@' and ch == t[from_index]:
            password_out = password_out + t[to_index]
            letter_found = True
        elif ch == '%' and ch == t[from_index]:
            password_out = password_out + t[to_index]
            letter_found = True

    if not letter_found:
        password_out = password_out + ch

# output
if encrypting:
    print('Your encrypted password is:', password_out)
else:
    print('Your decrypted password is:', password_out)
