# -*- coding: utf-8 -*-
"""
@author: podolnik
"""

def CheckBounds(r, c, r_max, c_max):
    if r >= 0 and r < r_max and c >= 0 and c < c_max:
        return True
    return False

def Next(maze, r, c, r_prev, c_prev, r_max, c_max):
    if CheckBounds(r_prev, c_prev, r_max, c_max):
        maze_e = maze[r][c]
        e_grid_top = maze[r - 1][c] if CheckBound
        
    elif r_prev == -1:
        return (0, c_prev + 1)
    
    raise Exception('Unknown previous location')
        
def main():
    input_file = 'aoc19-input.txt'
    
    maze = []
    
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            m_l = list(l.replace('\n', '').replace('\r', ''))
            maze.append(m_l)
        
    start_r = 0
    start_c = 0
    
    for i in range(len(maze[0])):
        if maze[0][i] == '|':
            start_c = i
            break
    
    print 'start', start_r, start_c
    
    r = start_r
    c = start_c
    r_prev = -1
    c_prev = start_c
    
    r_max = len(maze)
    c_max = len(maze_0)
    
    while True:
        maze_e = maze[r][c]
        
        if maze
        
if __name__ == "__main__":
    main()
