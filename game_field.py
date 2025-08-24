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
def mine_in_matrix(matrix_grid):
    for row in matrix_grid:
        random_row=random.randrange(consts.NUM_OF_ROWS)
        for col in row:
            random_col=random.randrange(consts.NUM_OF_COLS)
            if row==random_row and col ==random_col:
                matrix_grid[row][col]=="M"
    return matrix_grid
matrix_grid=mine_in_matrix(matrix_grid)
def print_matrix(matrix_grid):
    for m in matrix_grid:
        for n in m:
            print(n,end=" ")
        print()
print_matrix(matrix_grid)
