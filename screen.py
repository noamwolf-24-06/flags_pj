# import the pygame module
import pygame
import random
import consts
import game_field
import soldier

background_colour = consts.BACKGROUND_COLOR
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
screen.fill(background_colour)
pygame.display.flip()
pygame.display.set_caption('flag game')

def spawn_bushes():
    for i in range(consts.NUM_OF_BUSHES):
        x = random.randint(0,
                           consts.WINDOW_WIDTH - 50)  # Ensure the sprite fits within the screen
        y = random.randint(0, consts.WINDOW_HEIGHT - 50)
        draw_a_bush(x, y)


def draw_a_bush(x, y):
    GRASS = pygame.transform.scale(consts.GRASS_PNG, (50, 50))
    screen.blit(GRASS, (x, y))

def make_soldier():
    SOLDIER = pygame.transform.scale(soldier.SOLIDER_PNG, (80,80))
    return screen.screen.blit(SOLDIER,soldier.START_PLAYER)

def draw_grid():
    for x in range(consts.TILE_SIZE, consts.WINDOW_WIDTH, consts.TILE_SIZE):
        pygame.draw.line(screen, consts.COLOR_OF_GRID, (x, 0),
                         (x, consts.WINDOW_HEIGHT))
    for y in range(consts.TILE_SIZE, consts.WINDOW_HEIGHT, consts.TILE_SIZE):
        pygame.draw.line(screen, consts.COLOR_OF_GRID, (0, y),
                         (consts.WINDOW_WIDTH, y))


def draw_mine():
    MINE = pygame.transform.scale(consts.MINE_PNG, (60, 20))
    for i in range(consts.NUM_OF_ROWS):
        for j in range(consts.NUM_OF_COLS):
            if game_field.matrix_grid[i][j] == "M":
                coordinates = (j * (consts.TILE_SIZE)), (i * (consts.TILE_SIZE))
                screen.blit(MINE, coordinates)
def make_flag():
    FLAG = pygame.transform.scale(consts.FLAG_PNG,(80,60))
    return screen.blit(FLAG,consts.FLAG_COORDINATES)

def draw_screen():
    spawn_bushes()
    draw_grid()
    draw_mine()
    make_flag()
    # pygame.display.update()

draw_screen()
pygame.display.update()

# running = True
# part_one = True
#
# while running:
#      for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#      pygame.display.update()
draw_screen()