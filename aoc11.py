# -*- coding: utf-8 -*-

input_file = 'aoc11-input.txt'

path = []

lines = []

with open(input_file, 'r') as f:
    lines = f.readlines()

for l in lines:
    path.extend(l.strip().split(','))


def SimplifyPath(path):
    directions = ['s', 'n', 'sw', 'ne', 'nw', 'se']

    pairs = {
        ('s', 'n'): '',
        ('sw', 'ne'): '',
        ('nw', 'se'): '',
        ('n', 'sw'): 'nw',
        ('s', 'nw'): 'sw',
        ('s', 'ne'): 'se',
        ('n', 'se'): 'ne',
        ('ne', 'nw'): 'n',
        ('se', 'sw'): 's'
    }    
    
    path_len = len(path)
    
    simplified_path = {}
    
    for d in directions:
        simplified_path[d] = path.count(d)
        
    while True:
        for key in pairs:
            result = pairs[key]
            d_1 = key[0]
            d_2 = key[1]
            common_count = min(simplified_path[d_1], simplified_path[d_2])
            
            simplified_path[d_1] -= common_count
            simplified_path[d_2] -= common_count
            if not result == '':
                simplified_path[result] += common_count
        
        new_len = sum(simplified_path.itervalues())
        if new_len == path_len:
            return simplified_path
        else:
            path_len = new_len

simplified_path = SimplifyPath(path)
print 'final destination', sum(simplified_path.itervalues())
print simplified_path

max_distance = 0
max_len = 0

for i in range(len(path)):
    sub_path = path[:i+1]
    simplified_path = SimplifyPath(sub_path)
    dist = sum(simplified_path.itervalues())
    if dist > max_distance:
        max_distance = dist
        max_len = i + 1

print 'max distance', max_distance
simplified_path = SimplifyPath(path[:max_len])
print simplified_path