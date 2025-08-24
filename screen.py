# import the pygame module
import pygame
import random
import consts

background_colour = consts.BACKGROUND_COLOR
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption('Geeksforgeeks')
screen.fill(background_colour)
pygame.display.flip()
pygame.display.set_caption('flag game')


def spawn_bushes():
    for i in range(consts.NUM_OF_BUSHES):
        x = random.randint(0,
                           consts.WINDOW_WIDTH - 50)  # Ensure the sprite fits within the screen
        y = random.randint(0, consts.WINDOW_HEIGHT - 50)
        draw_a_bush(x,y)




x = 0
y = 0

def draw_a_bush(x, y):
    GRASS = pygame.transform.scale(consts.GRASS_PNG, (50,50))
    screen.blit(GRASS, (x, y))

spawn_bushes()
print("screen")


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
