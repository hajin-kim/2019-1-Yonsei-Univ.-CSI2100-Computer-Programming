# Read the file

texts = []

file = open('data.txt', 'r')

reader = file.readline()
while reader != '':
    texts.append(int(reader[:-1]))
    reader = file.readline()

file.close()

# Make the result

result = [(texts[0]*2 + texts[1])/3]

for i in range(0, len(texts)-2):
    result.append((texts[i] + texts[i+1] + texts[i+2])/3)

result.append((texts[-2] + texts[-1]*2)/3)

# Print

print(result)
