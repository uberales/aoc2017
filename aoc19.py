# -*- coding: utf-8 -*-
"""
@author: podolnik
"""

def M(maze, loc):
    return maze[loc[0]][loc[1]]

def Next(maze, loc, loc_prev, letters):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    maze_e = M(maze, loc)
    top = (loc[0] - 1, loc[1])
    bottom = (loc[0] + 1, loc[1])
    left = (loc[0], loc[1] - 1)
    right = (loc[0], loc[1] + 1)

    print loc, '(', maze_e, ')'

    if maze_e in alphabet:
        letters.append(maze_e)

    if maze_e == ' ':
        raise Exception('End found')
    if maze_e == '|' or maze_e == '-' or maze_e in alphabet:
        if loc_prev == top:
            return bottom
        elif loc_prev == bottom:
            return top
        elif loc_prev == left:
            return right
        elif loc_prev == right:
            return left
    elif maze_e == '+':
        directions = [top, left, bottom, right]
        start_i = directions.index(loc_prev)
        for i in range(len(directions) - 1):
            j = (i + start_i + 1) % len(directions)
            loc_j = directions[j]
            e_j = M(maze, loc_j)
            if e_j != ' ':
                return loc_j
        raise Exception('End found')

    raise Exception('Unknown maze combination: (' + maze_e + ')', loc, loc_prev)
        
def main():
    input_file = 'aoc19-input.txt'
    
    maze = []
    
    with open(input_file, 'r') as f:
        lines = f.readlines()
        i = 0
        row_l = 0
        for l in lines:
            m_l = [' ']
            m_l.extend(list(l.replace('\n', '').replace('\r', '')))
            m_l.append(' ')
            if i == 0:
                row_l = len(m_l)
                maze.append([' '] * row_l)
            i += 1
            maze.append(m_l)
        maze.append([' '] * row_l)

    start_r = 1
    start_c = 0
    
    for i in range(len(maze[start_r])):
        if maze[start_r][i] == '|':
            start_c = i
            break
    
    print 'start', start_r, start_c


    loc = (start_r, start_c)
    loc_prev = (start_r - 1, start_c)
    letters = []
    count = 0
    while True:
        try:
            loc_next = Next(maze, loc, loc_prev, letters)
            loc_prev = loc
            loc = loc_next
            count += 1
        except Exception, e:
            print e
            break
    print ''.join(letters)
    print count


if __name__ == "__main__":
    main()
