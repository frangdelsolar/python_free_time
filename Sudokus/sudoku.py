invalid_grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9]]

invalid_grid2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [2, 2, 2, 2, 2, 2, 2, 2, 2],
                 [3, 3, 3, 3, 3, 3, 3, 3, 3],
                 [4, 4, 4, 4, 4, 4, 4, 4, 4],
                 [5, 5, 5, 5, 5, 5, 5, 5, 5],
                 [6, 6, 6, 6, 6, 6, 6, 6, 6],
                 [7, 7, 7, 7, 7, 7, 7, 7, 7],
                 [8, 8, 8, 8, 8, 8, 8, 8, 8],
                 [9, 9, 9, 9, 9, 9, 9, 9, 0]]

valid_grid = [[3, 7, 1, 2, 8, 9, 5, 4, 6],
              [4, 8, 6, 1, 3, 5, 9, 7, 2],
              [2, 9, 5, 4, 7, 6, 8, 3, 1],
              [7, 3, 2, 6, 9, 8, 1, 5, 4],
              [8, 6, 9, 5, 1, 4, 3, 2, 7],
              [5, 1, 4, 7, 2, 3, 6, 9, 8],
              [9, 4, 3, 8, 6, 7, 2, 1, 5],
              [6, 2, 7, 9, 5, 1, 4, 8, 3],
              [1, 5, 8, 3, 4, 2, 7, 6, 9]]

COLUMN_COUNT = 9
ROW_COUNT = 9


def grid_is_valid(grid):
    if rows_are_valid(grid):
        print("Rows look good")
        if cols_are_valid(grid):
            print("Cols look good")
            if squares_are_valid(grid):
                print("Squares look good")
                return True
            print ("Flojo de cuadrados")
        print("Flojo de cols")
    print("Flojo de rows")
    return False


def rows_are_valid(grid):
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            if grid[row][col] == 0:
                return False
    return True


def cols_are_valid(grid):
    new_grid = []
    for row in range(ROW_COUNT):
        new_row = []
        for col in range(COLUMN_COUNT):
            new_row.append(grid[col][row])
        new_grid.append(new_row)
    return rows_are_valid(new_grid)


def squares_are_valid(grid):
    new_grid = []
    tuple = [(0, 3), (3, 6), (6, 9)]
    for par in tuple:
        a, b = par
        for par2 in tuple:
            c, d = par2
            new_row = []
            for row in range(a, b):
                for col in range(c, d):
                    new_row.append(grid[row][col])
            new_grid.append(new_row)
    return rows_are_valid(new_grid)


grid_is_valid(invalid_grid2)
grid_is_valid(invalid_grid)
grid_is_valid(valid_grid2)