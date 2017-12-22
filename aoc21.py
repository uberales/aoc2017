# -*- coding: utf-8 -*-
"""
@author: podolnik
"""

def GetGrid(pattern):
    rows = pattern.split("/")
    grid = []
    for r in rows:
        grid.append(list(r))
    return grid

def GetPattern(grid):
    pattern = '/'.join([''.join(r) for r in grid])
    return pattern

def NewGrid(dim):
    new_grid = []
    for i in range(dim):
        new_grid.append([''] * dim)
    return new_grid

def FlipUD(pattern):
    grid =  GetGrid(pattern)
    dim = len(grid)
    new_grid = NewGrid(dim)

    for r in range(dim):
        for c in range(dim):
            new_grid[dim - r - 1][c] = grid[r][c]

    return GetPattern(new_grid)

def FlipLR(pattern):
    grid =  GetGrid(pattern)
    dim = len(grid)
    new_grid = NewGrid(dim)

    for r in range(dim):
        for c in range(dim):
            new_grid[r][dim - c - 1] = grid[r][c]

    return GetPattern(new_grid)

def FlipD(pattern):
    grid =  GetGrid(pattern)
    dim = len(grid)
    new_grid = NewGrid(dim)

    for r in range(dim):
        for c in range(dim):
            new_grid[c][r] = grid[r][c]

    return GetPattern(new_grid)

def Rot90(pattern):
    grid = GetGrid(pattern)
    dim = len(grid)
    new_grid = NewGrid(dim)

    for r in range(dim):
        for c in range(dim):
            new_grid[c][dim - r - 1] = grid[r][c]

    return GetPattern(new_grid)

def AddFlipped(rules, pattern_in, pattern_out):
    pattern = FlipUD(pattern_in)
    AddRule(rules, pattern, pattern_out)
    pattern = FlipLR(pattern_in)
    AddRule(rules, pattern, pattern_out)
    pattern = FlipD(pattern_in)
    AddRule(rules, pattern, pattern_out)

def AddRule(rules, pattern_in, pattern_out):
    if not pattern_in in rules:
        rules[pattern_in] = pattern_out

def main():
    input_file = 'aoc21-input.txt'

    rules = {}

    with open(input_file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            data = l.strip().split(" ")
            pattern_in = data[0]
            pattern_out = data[2]
            rules[pattern_in] = pattern_out

    all_rules = {}

    print len(rules)

    for pattern_in in rules:
        #print 'transformed', pattern_in
        pattern_out = rules[pattern_in]
        AddFlipped(all_rules, pattern_in, pattern_out)
        pattern = Rot90(pattern_in)
        AddFlipped(all_rules, pattern, pattern_out)
        pattern = Rot90(pattern)
        AddFlipped(all_rules, pattern, pattern_out)
        pattern = Rot90(pattern)
        AddFlipped(all_rules, pattern, pattern_out)


    print len(all_rules)

    game_grid = GetGrid('.#./..#/###')

    for i in range(5):
        pattern_grid = []
        grid_dim = len(game_grid)
        step = 0
        if grid_dim % 2 == 0:
            step = 2
        elif grid_dim % 3 == 0:
            step = 3

        for r in range(0, grid_dim, step):
            p_row = []
            for c in range(0, grid_dim, step):
                sub_grid = game_grid[r:r + step][c:c + step]
                print sub_grid, r, r + step
                p_row.append(GetPattern(sub_grid))
            pattern_grid.append(p_row)

        print pattern_grid
        patt_dim = len(pattern_grid)
        new_grid = NewGrid((step + 1) * patt_dim)

        for r in range(patt_dim):
            for c in range(patt_dim):

                transformed = GetGrid(all_rules[pattern_grid[r][c]])
                t_dim = len(transformed)
                for r_t in range(t_dim):
                    for c_t in range(t_dim):
                        r_g = r * patt_dim + r_t
                        c_g = c * patt_dim + c_t
                        new_grid[r_g][c_g] = transformed[r_t][c_t]

        game_grid = new_grid
if __name__ == "__main__":
    main()
