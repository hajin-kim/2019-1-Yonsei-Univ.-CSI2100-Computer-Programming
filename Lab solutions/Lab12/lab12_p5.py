
from globals import FOODMAX, STEPMAX, WIDTH, HEIGHT, X_MAX, Y_MAX, MS_TO_QUIT
from globals import FOOD as food, GHOSTS as ghosts
# Import our own constants:

from characters import doboggi_man 

import turtle

class auto_doboggi_man(doboggi_man):

  """ Class auto_doboggi_man, the autonomous doboggi-collector.

      The auto_doboggi_man class is a subclass of the doboggi_man class. It
      inherits all data attributes and methods from the doboggi_man class. It
      overrides the move() method of the doboggi_man class to automatically
      navigate doboggi_man across the screen.

      Attributes:
         ... Please describe your attributes here
         move() method, including find_food() and avoid_ghost() function
  """

  def move(self):
    """
        Change this code to make your doboggi_man navigate the screen
        and collect all doboggi.
    """
    def find_food(pos):
      """
      Find the food and set direction to the food
      :param pos: [x, y] of food position
      :return: None
      """
      # Namespace
      x_distance = pos[0] - x
      y_distance = pos[1] - y
      direction = 'x'

      if not (-10 <= y_distance <= 10):
        if -1 < x_distance / y_distance < 1:
          direction = 'y'

      if direction == 'x':
        if x_distance < 0:
          self.turnWest()
        else:
          self.turnEast()
      elif direction == 'y':
        if y_distance < 0:
          self.turnSouth()
        else:
          self.turnNorth()

    def avoid_ghost(pos):
      """
      Determine whether move or not
      :param pos: [x, y] of ghost position
      :return: True if be allowed to move; False if not
      """
      # Namespace
      far_from_ghosts = x - pos[0]
      if far_from_ghosts < 0:
        far_from_ghosts += WIDTH

      if 140 < far_from_ghosts < WIDTH - 60:
        return True
      else:
        return False

    """Namespace"""
    # Get positions of self, foods, ghosts
    x = self.ttl.xcor()
    y = self.ttl.ycor()
    food_pos = []
    for i in food:
      food_pos.append(i.getPosition())
    ghosts_pos = []
    for i in ghosts:
      ghosts_pos.append(i.getPosition())

    # # Test code
    # print(food_pos)

    # Step 1. Find the first food
    if len(food_pos) == FOODMAX:
      find_food(food_pos[1])

    # Step 2. Move forward to the first ghost
    elif y < ghosts_pos[0][1] - 40:
      self.turnNorth()

    # Step 3. Avoid the first ghost
    elif y < ghosts_pos[0][1] - 30:
      if avoid_ghost(ghosts_pos[0]):
        self.turnNorth()
      else:
        return

    # Step 4. Move forward to the second ghost
    elif y < ghosts_pos[1][1] - 40:
      self.turnNorth()

    # Step 5. Avoid the second ghost
    elif y < ghosts_pos[1][1] - 30:
      if avoid_ghost(ghosts_pos[1]):
        self.turnNorth()
      else:
        return

    # Step 6. Move to safety area
    elif y < ghosts_pos[1][1] + 50:
      self.turnNorth()

    # Step 7. Find remaining foods
    else:
      find_food(food_pos[0])

    # Don't move beyond screen border
    if self.dir == 'east'  and self.ttl.xcor() > X_MAX:
      # self.turnWest()
      return
    if self.dir == 'west'  and self.ttl.xcor() < -X_MAX:
      # self.turnEast()
      return
    if self.dir == 'north' and self.ttl.ycor() > Y_MAX:
      # self.turnSouth()
      return
    if self.dir == 'south' and self.ttl.ycor() < -Y_MAX:
      # self.turnNorth()
      return

    # Move forward
    self.ttl.forward(10)

    #
    # Uncomment to dump positions in the PyCharm console window:
    #
    # print(ghosts[0], ghosts[1])
    # print(food[0], food[1], food[2])
