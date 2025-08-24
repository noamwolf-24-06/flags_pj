import consts
def create_matrix():
    game_grid=[]
    for i in range(consts.NUM_OF_ROWS):
        row = []
        for j in range(consts.NUM_OF_COLS):
            row.append(0)
        game_grid.append(row)
    return game_grid
matrix_grid=create_matrix()
def print_matrix(matrix_grid):
    for m in matrix_grid:
        for n in m:
            print(n,end=" ")
        print()
print_matrix(matrix_grid)