# -*- coding: utf-8 -*-
"""
@author: podolnik
"""

import copy

def Turn(direction, way):
    d_top = (-1, 0)
    d_left = (0, -1)
    d_bottom = (1, 0)
    d_right = (0, 1)
    directions = [d_top, d_left, d_bottom, d_right]
    
    if way == 'left':
        curr_i = directions.index(direction)
        next_i = (curr_i + 1) % 4
        return directions[next_i]
    elif way == 'right':
        curr_i = directions.index(direction)
        next_i = (curr_i - 1) % 4
        return directions[next_i]
    elif way == 'back':
        curr_i = directions.index(direction)
        next_i = (curr_i - 2) % 4
        return directions[next_i]
    
    raise Exception('Unknown way')

        
def main():
    input_file = 'aoc22-input.txt'
    
    field = []
    
    extra = 200
    
    with open(input_file, 'r') as f:
        lines = f.readlines()
        row_l = -1
        for l in lines:
            row = list(l.strip())
            if row_l == -1:
                row_l = len(row)
                for i in range(extra):
                    e_row = ['.'] * (2 * extra + row_l)
                    field.append(e_row)
            ext_row = ['.'] * extra
            ext_row.extend(row)
            ext_row.extend(['.'] * extra)
            field.append(ext_row)
        for i in range(extra):
            e_row = ['.'] * (2 * extra + row_l)
            field.append(e_row)
    
    backup_field = copy.deepcopy(field)
    field_size = len(field)
    position = ((field_size + 1) / 2 - 1, (field_size + 1) / 2 - 1)
    direction = (-1, 0)
    infections = 0
    
    for i in range(10000):
        node = field[position[0]][position[1]]
        if node == '#':
            direction = Turn(direction, 'right')
            field[position[0]][position[1]] = '.'
        else:
            direction = Turn(direction, 'left')
            field[position[0]][position[1]] = '#'
            infections += 1
        position = (position[0] + direction[0], position[1] + direction[1])
    
    #print '\n'.join([''.join(l) for l in field])
    print infections
        
    field = copy.deepcopy(backup_field)
    position = ((field_size + 1) / 2 - 1, (field_size + 1) / 2 - 1)
    direction = (-1, 0)
    infections = 0
    
    for i in range(10000000):
        node = field[position[0]][position[1]]
        if node == '#':
            direction = Turn(direction, 'right')
            field[position[0]][position[1]] = 'f'
        elif node == 'w':
            field[position[0]][position[1]] = '#'
            infections += 1
        elif node == 'f':
            direction = Turn(direction, 'back')
            field[position[0]][position[1]] = '.'
        else:
            direction = Turn(direction, 'left')
            field[position[0]][position[1]] = 'w'
        position = (position[0] + direction[0], position[1] + direction[1])
    
    #print '\n'.join([''.join(l) for l in field])
    print infections
        
if __name__ == "__main__":
    main()

[
['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
['.', '.', '.', '.', '.', '#', '.', '.', '.'], 
['.', '.', 'w', 'w', 'w', '.', '.', '.', '.'], 
['.', '.', 'w', 'w', '.', '.', '.', '.', '.'], 
['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
['.', '.', '.', '.', '.', '.', '.', '.', '.']]
