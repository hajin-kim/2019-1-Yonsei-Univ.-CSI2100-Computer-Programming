# Sparse Text Program

def createModifiedFile(input_file, outputfile):
    '''
        For text file input_file, creates a new version in file outputfile
        in which all instances of the letter 'e' are removed.
    '''
    
    empty_str = ''
    num_total_chars = 0
    num_removals = 0

    text_orig = ''
    for line in input_file:
        text_orig += line
    # print(text_orig)

    text_no_eol = text_orig.split('\n')
    # print(text_no_eol)

    for i in range(0, len(text_no_eol)):
        line = text_no_eol[i]

        # save original line length
        orig_line_length = len(line)
        num_total_chars = num_total_chars + orig_line_length

        # remove all occurrances of vowels
        modified_line = line.replace('a', empty_str).replace('A', empty_str).\
            replace('e', empty_str).replace('E', empty_str).\
            replace('i', empty_str).replace('I', empty_str).\
            replace('o', empty_str).replace('O', empty_str).\
            replace('u', empty_str).replace('U', empty_str)
        num_removals = num_removals + \
                         (orig_line_length - (len(modified_line)))

        # simulataneouly output line to screen and output file
        #
        # Feedback : -5(100%) one more print statement is executed if eol exists
        # # Old code
        # print(modified_line)
        # if i == len(text_no_eol) - 1:
        #     output_file.write(modified_line)
        # else:
        #     output_file.write(modified_line+'\n')
        #
        if i == len(text_no_eol) - 1:
            output_file.write(modified_line)
            if modified_line != '':
                print(modified_line)
        else:
            output_file.write(modified_line+'\n')
            print(modified_line)
        #
        # Feedback completed
        #

    # for line in input_file:
    #
    #     # save original line length
    #     orig_line_length = len(line) - 1
    #     num_total_chars = num_total_chars + orig_line_length
    #
    #     # remove all occurrances of vowels
    #     modified_line = line.replace('a', empty_str).replace('A', empty_str).\
    #         replace('e', empty_str).replace('E', empty_str).\
    #         replace('i', empty_str).replace('I', empty_str).\
    #         replace('o', empty_str).replace('O', empty_str).\
    #         replace('u', empty_str).replace('U', empty_str)
    #     num_removals = num_removals + \
    #                      (orig_line_length - (len(modified_line)-1))
    #
    #     # simulataneouly output line to screen and output file
    #     print(modified_line.strip('\n'))
    #     output_file.write(modified_line)

    return (num_total_chars, num_removals)


# --- main

# open files for reading and writing
file_name = input('Enter file name (including file extension): ')
input_file = open(file_name,'r')
new_file_name = 'new_' + file_name
output_file = open(new_file_name, 'w')
#
# Test code - alice
# file_name = 'lab11_p1 output test\\alice_tea_party.txt'
# input_file = open(file_name,'r')
# new_file_name = 'lab11_p1 output test\\new_alice_tea_party.txt'
# output_file = open(new_file_name, 'w')
#
# Test code - extra 1
# file_name = 'lab11_p1 output test\\text_no_eol.txt'
# input_file = open(file_name,'r')
# new_file_name = 'lab11_p1 output test\\new_text_no_eol.txt'
# output_file = open(new_file_name, 'w')
#
# createModifiedFile(input_file, output_file)
# input_file.close()
# output_file.close()
#
# Test code - extra 2
# file_name = 'lab11_p1 output test\\text_with_eol.txt'
# input_file = open(file_name,'r')
# new_file_name = 'lab11_p1 output test\\new_text_with_eol.txt'
# output_file = open(new_file_name, 'w')
#
# createModifiedFile(input_file, output_file)
# input_file.close()
# output_file.close()
#
# Test code - extra 3
# file_name = 'lab11_p1 output test\\text_with_many_eol.txt'
# input_file = open(file_name,'r')
# new_file_name = 'lab11_p1 output test\\new_text_with_many_eol.txt'
# output_file = open(new_file_name, 'w')
#
# createModifiedFile(input_file, output_file)
# input_file.close()
# output_file.close()
#
# Test code - extra 4
# file_name = 'lab11_p1 output test\\text_no.txt'
# input_file = open(file_name,'r')
# new_file_name = 'lab11_p1 output test\\new_text_no.txt'
# output_file = open(new_file_name, 'w')


# create file with all letter e removed
print()
num_total_chars, num_removals = createModifiedFile(input_file, output_file)

# close current input and output files
input_file.close()
output_file.close()

# display percentage of characters removed
print()
print(num_removals, "vowels removed")
print(num_removals, "out of", num_total_chars, "characters removed")
print('Percentage of data lost:',
      int((num_removals / num_total_chars) * 100), '%')
print('Modified text in file', new_file_name)

# Feedback : -5(100%) one more print statement is executed if eol exists
