# Read the file

texts = []

file = open('data.txt', 'r')
# file = open('data lab10_p4 Feedback.txt', 'r')    # Feedback test code

reader = file.readline()
while reader != '':
    texts.append(int(reader[:-1]))
    reader = file.readline()

file.close()

# Make the result

#
# Feedback : -6.25(25%) list out of range exception when the number of the input is only one
# # Old code
#
# result = [(texts[0]*2 + texts[1])/3]
#
# for i in range(0, len(texts)-2):
#     result.append((texts[i] + texts[i+1] + texts[i+2])/3)
#
# result.append((texts[-2] + texts[-1]*2)/3)
#
result = []

x1 = [texts[0]] + texts + [texts[-1]]

for i in range(0, len(x1)-2):
    result.append( ( x1[i] + x1[i+1] + x1[i+2] ) / 3)
#
# Feedback completed
#

# Print

print(result)

# Feedback : -6.25(25%) list out of range exception when the number of the input is only one
