# Importing pygame module
import pygame
from pygame.locals import *

import consts
import soldier
import screen
from screen import draw_a_bush

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

SOLDIER = pygame.transform.scale(soldier.SOLIDER_PNG,(80,80))
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

# Add caption in the window
pygame.display.set_caption('Player Movement')
screen.spawn_bushes()

# Store the initial
# coordinates of the player in
# two variables i.e. x and y.
x = 0
y = 0
screen.screen.fill(consts.BACKGROUND_COLOR)

# Create a variable to store the
# velocity of player's movement
velocity = 20

# Creating an Infinite loop
run = True
while run:
    # Filling the background with
    # white color
    screen.screen.fill(consts.BACKGROUND_COLOR)
    screen.make_flag()


    # Display the player sprite at x
    # and y coordinates
    window.blit(SOLDIER, (x, y))

    # iterate over the list of Event objects
    # that was returned by pygame.event.get()
    # method.
    for event in pygame.event.get():

        # Closing the window and program if the
        # type of the event is QUIT
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        # Checking event key if the type
        # of the event is KEYDOWN i.e.
        # keyboard button is pressed
        if event.type == pygame.KEYDOWN:

            # Decreasing the x coordinate
            # if the button pressed is
            # Left arrow key
            if event.key == pygame.K_LEFT:
                x -= velocity

            # Increasing the x coordinate
            # if the button pressed is
            # Right arrow key
            if event.key == pygame.K_RIGHT:
                x += velocity

            # Decreasing the y coordinate
            # if the button pressed is
            # Up arrow key
            if event.key == pygame.K_UP:
                y -= velocity

            if event.key == pygame.K_KP_ENTER:
                screen.screen.fill('black')
                screen.draw_grid()
                screen.draw_mine()

            # Increasing the y coordinate
            # if the button pressed is
            # Down arrow key
            if event.key == pygame.K_DOWN:
                y += velocity
        pygame.display.update()
