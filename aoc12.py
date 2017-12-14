# -*- coding: utf-8 -*-

input_file = 'aoc12-input.txt'

path = []

programs = {}

with open(input_file, 'r') as f:
    lines = f.readlines()

for l in lines:
    parts = [int(p) for p in l.strip().replace(',', '').replace('<-> ', '').split(' ')]
    programs[parts[0]] = parts[1:]

def GetGroup(programs, pivot):
    
    group = set([pivot])
    pipes = programs[pivot]
    to_process = set(pipes)
    
    while len(to_process) > 0:
        current = to_process.pop()
        pipes = programs[current]
        if not current in group:
            group.add(current)
            to_process = to_process.union(set(pipes))
    
    return group

program_ids = set(programs.keys())
group_0 = GetGroup(programs, 0)
print 'group 0:', len(group_0)

count = 0
while len(program_ids) > 0:
    g = GetGroup(programs, program_ids.pop())
    program_ids = program_ids.difference(g)
    print len(g), g
    count += 1

print 'total:', count