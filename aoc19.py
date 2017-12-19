# -*- coding: utf-8 -*-
"""
@author: podolnik
"""

def Next(maze, loc, loc_prev, letters):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    maze_e = maze[loc[0]][loc[1]]
    top = (loc[0] - 1, loc[1])
    bottom = (loc[0] + 1, loc[1])
    left = (loc[0], loc[1] - 1)
    right = (loc[0], loc[1] + 1)

    directions = [top, left, bottom, right]
    start_i = directions.index(loc_prev)
    dir_count = len(directions)
    print loc, '(', maze_e, ')'

    if maze_e in alphabet:
        letters.append(maze_e)

    if maze_e == ' ':
        raise Exception('End found')
    if maze_e == '|' or maze_e == '-' or maze_e in alphabet:
        return directions[(start_i  + 2) % dir_count]
    elif maze_e == '+':
        for i in range(dir_count - 1):
            j = (i + start_i + 1) % dir_count
            loc_j = directions[j]
            e_j = maze[loc_j[0]][loc_j[1]]
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
