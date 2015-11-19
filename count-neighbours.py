def count_neighbours(grid, row, col):
    
    start_row = row if row == 0 else row - 1
    end_row = row if row == len(grid) - 1 else row + 1
    
    start_col = col if col == 0 else col - 1
    end_col = col if col == len(grid[row]) - 1 else col + 1
    
    res = 0
    
    # print(start_row, end_row, start_col, end_col)
    
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            # print(i, j)
            if i == row and j == col:
                continue
            if grid[i][j] == 1:
                res += 1
    
    return res;

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
