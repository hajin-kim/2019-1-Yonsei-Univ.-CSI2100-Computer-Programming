# (C) Wiley (the textbook publisher).
#
# The programs in this folder are provided for your personal studies only.
# You are NOT allowed to publish this program in any form.
# - Do not put it on a public source repository like github.
# - Do not put it on a web-site or similar.

# Horse Racing Program

import turtle
import random
import time


def getHorseImages(num_horses):
    """
    Get icons of horses
    :param num_horses: The number of horses
    :return: Images
    """
    # init empty list
    images = []

    # get all horse images
    for k in range(0, num_horses):
        images = images + ['img/horse_' + str(k + 1) + '_image.gif']

    return images


def getBannerImages(num_horses):
    """
    Get icons of banner
    :param num_horses: The number of horses
    :return: Images
    """
    # init empty list
    all_images = []

    # get "They're Off" banner image
    images = ['img/theyre_off_banner.gif']
    all_images.append(images)

    # get early lead banner images
    images = []
    for k in range(0, num_horses):
        images = images + ['img/lead_at_start_' + str(k + 1) + '.gif']
    all_images.append(images)

    # get mid-way lead banner images
    images = []
    for k in range(0, num_horses):
        images = images + ['img/looking_good_' + str(k + 1) + '.gif']
    all_images.append(images)

    # get "We Have a Winner" banner image
    images = ['img/winner_banner.gif']
    all_images.append(images)

    return all_images


def registerHorseImages(images):
    """
    Register images to horses
    :param images: Image objects
    :return: None
    """
    for k in range(0, len(images)):
        turtle.register_shape(images[k])    # Registering


def registerBannerImages(images):
    """
    Register images to banners
    :param images: Image objects
    :return: None
    """
    for k in range(0, len(images)):
        for j in range(0, len(images[k])):
            turtle.register_shape(images[k][j]) # Registering


def newHorse(image_file):
    """
    Make a new horse
    :param image_file: Get image
    :return: Horse object
    """
    horse = turtle.Turtle()
    horse.hideturtle()
    horse.shape(image_file)

    return horse    # Return the object


def generateHorses(images, num_horses):
    """
    Genarate horses
    :param images: Get image
    :param num_horses: Horse object
    :return: Horses objects in list
    """
    horses = []
    for k in range(0, num_horses):
        horse = newHorse(images[k])
        horses.append(horse)

    return horses   # Return in list


def placeHorses(horses, loc, separation):
    """
    Set location
    :param horses: Given horses objects
    :param loc: Location
    :param separation: Between them
    :return: None
    """
    for k in range(0, len(horses)):
        horses[k].hideturtle()
        horses[k].penup()
        horses[k].setposition(loc[0], loc[1] + k * separation)  # Move
        horses[k].setheading(180)
        horses[k].showturtle()
        horses[k].pendown()


def findLeadHorse(horses):
    """
    Find leading horse
    :param horses: list
    :return: Leading horse
    """
    # init
    lead_horse = 0

    for k in range(1, len(horses)):
        if horses[k].position()[0] < \
                horses[lead_horse].position()[0]:
            lead_horse = k
    return lead_horse


def displayBanner(banner, position):
    """
    Show banner
    :param banner: banner
    :param position: location in list
    :return: None
    """
    the_turtle = turtle.getturtle()
    turtle.setposition(position[0], position[1])
    turtle.shape(banner)
    turtle.stamp()  # Show banner


def startHorses(horses, banners, finish_line, forward_incr):
    """
    Until having winner
    :param horses: List
    :param banners: List
    :param finish_line: Goal
    :param forward_incr: Incresaing amount
    :return: Index of winner
    """
    # init
    have_winner = False
    early_leading_horse_displayed = False
    midrace_leading_horse_displayed = False

    # display "there're off" banner
    displayBanner(banner_images[0][0], (70, -300))

    k = 0
    while not have_winner:
        horse = horses[k]
        horse.forward(random.randint(1, 3) * forward_incr)

        # display mid-race lead banner
        lead_horse = findLeadHorse(horses)
        if horses[lead_horse].position()[0] < -125 and \
                not midrace_leading_horse_displayed:

            displayBanner(banners[2][lead_horse], (40, -300))
            midrace_leading_horse_displayed = True

        # display early lead banner
        elif horses[lead_horse].position()[0] < 125 and \
                not early_leading_horse_displayed:
            displayBanner(banners[1][lead_horse], (10, -300))
            early_leading_horse_displayed = True

        # check for horse over finish line
        if horse.position()[0] < finish_line:
            have_winner = True
        else:
            k = (k + 1) % len(horses)
    return k


def displayWinner(winning_horse, winner_banner):
    """
    Display winner
    :param winning_horse: Won horse
    :param winner_banner: Image
    :return: None
    """
    # display "We Have a Winner" banner
    displayBanner(winner_banner, (20, -300))

    # blink winning horse
    show = False
    counter = 10
    while counter != 0:
        if show:
            winning_horse.showturtle()
            show = False
        else:
            winning_horse.hideturtle()
            show = True

        counter = counter - 1
        time.sleep(.4)


# ---- main

# init number of horses
num_horses = 10
win_times = []
horse_range = list(range(0, num_horses))
for k in horse_range:
    win_times.append(0)

# set window size
turtle.setup(750, 800)

# get turtle window
window = turtle.Screen()

# set window title bar
window.title('Horse Race Simulation Program')


# Use while loop with Boolean flag
rerun_flag = True

while rerun_flag:
    # hide default turtle and keep from drawing
    turtle.hideturtle()
    turtle.penup()

    # init screen layout parameters
    start_loc = (240, -200)
    finish_line = -240
    track_separation = 60
    forward_incr = 6

    # register images
    horse_images = getHorseImages(num_horses)
    banner_images = getBannerImages(num_horses)
    registerHorseImages(horse_images)
    registerBannerImages(banner_images)

    # generate and init horses
    horses = generateHorses(horse_images, num_horses)

    # place horses at starting line
    placeHorses(horses, start_loc, track_separation)

    # start horses
    winner = startHorses(horses, banner_images, finish_line,
                         forward_incr)

    # light up for winning horse
    displayWinner(horses[winner], banner_images[3][0])

    win_times[winner] += 1

    # Loop with Boolean flag
    if str(input('Press \'q\' to quit: ')) == 'q':
        rerun_flag = False
    else:
        for i in horse_range:
            horses[i].clear()

# terminate program when close window
turtle.bye()

# Print win times
for l in horse_range:
    print('Horse', l+1, 'won', win_times[l], 'times')
