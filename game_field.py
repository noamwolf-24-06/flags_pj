import consts
import random
def create_matrix():
    game_grid=[]
    for i in range(consts.NUM_OF_ROWS):
        row = []
        for j in range(consts.NUM_OF_COLS):
            row.append(0)
        game_grid.append(row)
    return game_grid
matrix_grid=create_matrix()
def flag_loc(matrix_grid):
    for i in range(4,0,-1):
        for j in range(3,0,-1):
            matrix_grid[consts.NUM_OF_ROWS-j-1][consts.NUM_OF_COLS-i]="F"
    return matrix_grid
matrix_grid=flag_loc(matrix_grid)
def mine_in_matrix(matrix_grid):
    for i in range (20):
        random_row = random.randrange(consts.NUM_OF_ROWS)
        random_col = random.randrange(consts.NUM_OF_COLS)
        if matrix_grid[random_row][random_col]=="F" or random_col>47 or (random_col>46 and random_row==24):
            random_row = random.randrange(consts.NUM_OF_ROWS)
            random_col = random.randrange(consts.NUM_OF_COLS)
        for row in range(len(matrix_grid)):
            for col in range(len(matrix_grid[row])):
                if row==random_row and col == random_col:
                    matrix_grid[row][col]="M"
    return matrix_grid
matrix_grid=mine_in_matrix(matrix_grid)
def print_matrix(matrix_grid):
    for m in matrix_grid:
        for n in m:
            print(n, end=" ")
        print()
print_matrix(matrix_grid)