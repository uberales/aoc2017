# -*- coding: utf-8 -*-
"""
@author: podolnik
"""

import numpy as np

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

def FlipD2(pattern):
    grid =  GetGrid(pattern)
    dim = len(grid)
    new_grid = NewGrid(dim)

    for r in range(dim):
        for c in range(dim):
            new_grid[dim - c - 1][dim - r - 1] = grid[r][c]

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
    AddRule(rules, pattern_in, pattern_out)
    pattern = FlipUD(pattern_in)
    AddRule(rules, pattern, pattern_out)
    pattern = FlipLR(pattern_in)
    AddRule(rules, pattern, pattern_out)
    pattern = FlipD(pattern_in)
    AddRule(rules, pattern, pattern_out)
    pattern = FlipD2(pattern_in)
    AddRule(rules, pattern, pattern_out)

def AddRule(rules, pattern_in, pattern_out):
    rules[pattern_in] = pattern_out
    
def FractalArt(input_pattern, rules, iterations):
    game_grid = np.array(GetGrid(input_pattern))

    for i in range(iterations):
        pattern_grid = []
        grid_dim = len(game_grid)
        
        step = 3
        if grid_dim % 2 == 0:
            step = 2
            
        for r in range(0, grid_dim, step):
            p_row = []
            for c in range(0, grid_dim, step):
                sub_grid = game_grid[r:r + step,c:c + step]
                p_row.append(GetPattern(sub_grid))
            pattern_grid.append(p_row)

        patt_dim = len(pattern_grid)
        new_grid = NewGrid((step + 1) * patt_dim)

        for r in range(patt_dim):
            for c in range(patt_dim):
                grid_transformed = GetGrid(rules[pattern_grid[r][c]])
                t_dim = len(grid_transformed)
                for r_t in range(t_dim):
                    for c_t in range(t_dim):
                        r_g = r * t_dim + r_t
                        c_g = c * t_dim + c_t
                        new_grid[r_g][c_g] = grid_transformed[r_t][c_t]

        game_grid = np.array(new_grid)

    return game_grid

def CountCrosses(game_grid):
    crosses = 0
    for r in range(len(game_grid)):
        for c in range(len(game_grid)):
            if game_grid[r, c] == "#":
                crosses += 1
    return crosses
    
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

    for pattern_in in rules:
        pattern_out = rules[pattern_in]
        AddFlipped(all_rules, pattern_in, pattern_out)
        pattern = Rot90(pattern_in)
        AddFlipped(all_rules, pattern, pattern_out)
        pattern = Rot90(pattern)
        AddFlipped(all_rules, pattern, pattern_out)
        pattern = Rot90(pattern)
        AddFlipped(all_rules, pattern, pattern_out)

    input_pattern = '.#./..#/###'
    
    game_grid = FractalArt(input_pattern, all_rules, 5)
    crosses = CountCrosses(game_grid)    
    print crosses
    
    game_grid = FractalArt(input_pattern, all_rules, 18)
    crosses = CountCrosses(game_grid)    
    print crosses
    
if __name__ == "__main__":
    main()
