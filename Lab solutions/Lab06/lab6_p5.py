from operator import itemgetter

fruitlist = []
sortedlist = []
i = 0

fruit_type = str(input('Enter a fruit type (q to quit): '))

# If first input is q, execute only one print statement.
if fruit_type == 'q':
    print('No data received, exiting.')
else:
    while fruit_type != 'q':
        fruitlist.append( [fruit_type, int( input('Enter the weight in kg: ')) ] )
        fruit_type = str(input('Enter a fruit type (q to quit): '))

    fruitlist.sort( key=itemgetter(0) )
    sortedlist.append(fruitlist[0])

    for j in range(len(fruitlist) -1):
        if fruitlist[j][0] == fruitlist[j+1][0]:
            sortedlist[i][1] += fruitlist[j+1][1]
        else:
            sortedlist.append(fruitlist[j+1])
            i += 1

    # print(len(fruitlist))
    # print(len(sortedlist))
    # print(i)

    for k in range(i+1):
        print(sortedlist[k][0]+', '+str(sortedlist[k][1])+'kg.')
