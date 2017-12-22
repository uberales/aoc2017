# -*- coding: utf-8 -*-
"""
@author: podolnik
"""

import numpy as np

def GetGrid(pattern):
    grid = [list(r) for r in pattern.split("/")]
    return grid

def GetPattern(grid):
    pattern = '/'.join([''.join(r) for r in grid])
    return pattern

def NewGrid(dim):
    new_grid = [[''] * dim for i in range(dim)]
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

def FlipD1(pattern):
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
    pattern = FlipD1(pattern_in)
    AddRule(rules, pattern, pattern_out)
    pattern = FlipD2(pattern_in)
    AddRule(rules, pattern, pattern_out)

def AddRule(rules, pattern_in, pattern_out):
    rules[pattern_in] = pattern_out
    
def FractalArt(input_pattern, rules, iterations):
    game_grid = np.array(GetGrid(input_pattern))

    for i in range(iterations):
        grid_dim = len(game_grid)
        
        step = 3
        if grid_dim % 2 == 0:
            step = 2
        
        new_dim = (step + 1) * (grid_dim / step)
        new_grid = np.array(NewGrid(new_dim))
            
        for r in range(0, grid_dim, step):
            for c in range(0, grid_dim, step):
                sub_grid = game_grid[r:r + step, c:c + step]
                sub_pattern = GetPattern(sub_grid)
                
                rule_grid = GetGrid(rules[sub_pattern])
                rule_size = step + 1
                
                r_g_min = (r / step) * rule_size
                c_g_min = (c / step) * rule_size
                r_g_max = r_g_min + rule_size
                c_g_max = c_g_min + rule_size
                                
                new_grid[r_g_min:r_g_max, c_g_min:c_g_max] = rule_grid[0:rule_size][0:rule_size]
        
        game_grid = new_grid

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
