import time
import copy
import turtle

SIZE=20 # size of the 2D cellular automaton
work = []
tmp  = []


def printSep():
    '''Print a separator'''
    for ctr in range(0, SIZE+2):
        print('-', end='')
    print('')


def printWorld(world):  # Changed HJ
    '''Print one generation.
       Must use printSep() above to print the separators. 
    '''
    # Test codes start
    # test_file.write('-'*(SIZE+2)+'\n')
    # Test codes end
    printSep()
    for i in range(0, SIZE):
        assist_string = printEachRow(world, i)
        # Test codes start
        # test_file.write(assist_string+'\n')
        # Test codes end
        print(assist_string)
    printSep()
    # Test codes start
    # test_file.write('-'*(SIZE+2)+'\n')
    # Test codes end


def printEachRow(world, row_num):
    """
    Return one row as string
    :param world: result of work
    :param row_num: interested row number
    :return: one row as string
    """
    string_append = '|'
    for i in range(0, SIZE):
        if world[row_num][i]:
            string_append += 'x'    # Mean being alive
        else:
            string_append += ' '
    string_append += '| row ' + str(row_num)
    return string_append


def cellDiscriminator(cell_state, sum_up):
    """
    Discriminate whether cell is going to be alive or dead
    :param cell_state: recent state of interested cell
    :param sum_up: sum by cellSum()
    :return: alive = 1, dead = 0
    """
    discriminator = sum_up * 2 - cell_state
    if (5 <= discriminator) and (discriminator <= 7):
        return 1    # Mean being alive
    else:
        return 0    # Mean being dead


def cellSum(world_tmp, y, x):
    """
    Get sum of around cells alive, including interested cell itself
    :param world_tmp: work
    :param y: location
    :param x: location
    :return: sum as integer
    """
    cellSum_result = 0
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if i >=0 and j >= 0 and i < SIZE and j < SIZE:  # Edge limitation
                cellSum_result += world_tmp[i][j]
            else:
                cellSum_result += 0
    return cellSum_result


def getSize():
    """
    Get SIZE
    :return: SIZE
    """
    try:
        inp_size = int(input('Grid sidelength (default 20): '))
        if inp_size < 20:
            return 20
        else:
            return inp_size
    except:
        return 20   # Use default


def getGeneration():
    """
    Get GENE
    This function can call itself
    :return: GENE or this function itself
    """
    try:
        inp_generation = int(input('Max generation: '))
        if inp_generation <= 0:
            return getGeneration()
        else:
            return inp_generation
    except:
        return getGeneration()  # Call itself


def setDrawer(drawer, square_size, cell, x, y):
    """
    Set drawer
    :param drawer: turtle
    :param square_size: size of square
    :param cell: cell state
    :param x: location
    :param y: location
    :return: none
    """
    # For turtle
    drawer.penup()
    drawer.shape('square')
    if cell:
        drawer.showturtle()
    drawer.resizemode('user')
    drawer.turtlesize((square_size - 1 - 0) / 20, (square_size - 1 - 0) / 20)
    drawer.speed(0)
    drawer.setposition(square_size * x, square_size * y)


#
# Main program
#

# Initialize work
for i in range(0, 3):
    work.append([0, 1] + [0] * 18)
for i in range(3, 10):
    work.append([0] * 20)
work.append([0] * 10 + [1] * 3 + [0] * 7)
work.append([0] * 10 + [1] + [0] * 9)
work.append([0] * 10 + [1] * 3 + [0] * 7)
for i in range(13, 20):
    work.append([0] * 20)

# Test code
# print(work)

#
# Test codes start HJ
#
# Initialize work
#

# read_file = open('cellular_automaton\\SampleOutput.txt')
# read_file.readline()
# for r in range(0, 20):
#     temp_string = read_file.readline()
#     temp_string = temp_string.replace(' ', '0')
#     temp_string = temp_string.replace('x', '1')
#     temp_list = []
#     for r2 in range(1, 21):
#         temp_list.append(int(temp_string[r2]))
#     work.append(temp_list)
# read_file.close()

#
# Test codes end HJ
#

# Compute:
SIZE = getSize()
GENE = getGeneration()

# Test code
# Output file
# test_file = open('lab11_p2_output_test\\lab11_p2_output s'+str(SIZE)+' g'+str(GENE)+'.txt', 'w')

window_size = 600
square_size = window_size / SIZE

# Append work
if SIZE > 20:
    for r in range(0, 20):
        for r2 in range(20, SIZE):
            work[r].append(0)
    for r3 in range(20, SIZE):
        work.append([0]*SIZE)

# Turtle
turtle.setup(window_size+2*square_size, window_size-20)
turtle.screensize(window_size, window_size-20)
turtle.setworldcoordinates(0, window_size-20, window_size+2*square_size, 0)
turtle.tracer(0, 0)
window = turtle.Screen()

# Row number.
# Made on 6.5 Wed. 22:35.
point = turtle.Turtle()
point.penup()
point.hideturtle()
for i in range(0, SIZE):
    point.setposition(window_size, int(i*square_size+square_size//6))
    point.write(' row '+str(i), font = ('Times New Roman', int(square_size/2), 'bold'))

drawer = []
# Make turtles and draw gene 0
for y in range(0, SIZE):
    drawer.append([])
    for x in range(0, SIZE):
        drawer[y].append(turtle.Turtle())
        drawer[y][x].hideturtle()
        setDrawer(drawer[y][x], square_size, work[y][x], x, y)
turtle.update()

window.listen()

# # Print gene 0
# printWorld(work)
# Intensive time sleep
time.sleep(1)

# Print gene 1 ~ GENE
while GENE:
    tmp = copy.deepcopy(work)

    # Now discrimination is by variable tmp
    # Now mutation is to variable work
    for y in range(0, SIZE):
        for x in range(0, SIZE):
            work[y][x] = \
                cellDiscriminator(tmp[y][x], cellSum(tmp, y, x))

    # Draw cells
    for y in range(0, SIZE):
        for x in range(0, SIZE):
            if work[y][x]+tmp[y][x] == 1:
                if tmp[y][x]:
                    drawer[y][x].hideturtle()
                else:
                    drawer[y][x].showturtle()
    turtle.update()

    # # Print cells
    # printWorld(work)
    # Intensive time sleep
    time.sleep(1)

    GENE -= 1


# turtle.mainloop()
# Test code
# Output file
# test_file.close()
