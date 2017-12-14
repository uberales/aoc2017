# -*- coding: utf-8 -*-

input_file = 'aoc13-input.txt'

firewall = []

with open(input_file, 'r') as f:
    lines = f.readlines()

for l in lines:
    parts = [int(p) for p in l.strip().replace(':', '').split(' ')]
    firewall.append((parts[0], parts[1]))

def ScannersAtTime(firewall, time):
    scanners = []
    for i in range(len(firewall)):
        level = firewall[i]
        offset = level[0]
        depth = level[1]
        time_at_level = time + offset
                
        if time_at_level % (2 * depth - 2) == 0:
            scanners.append(depth * offset)
        else:
            scanners.append(0)
        
    return scanners
    
def IsOpen(firewall, time):
    for i in range(len(firewall)):
        level = firewall[i]
        offset = level[0]
        depth = level[1]
        time_at_level = time + offset
                
        if time_at_level % (2 * depth - 2) == 0:
            return False
        
    return True
    
delta = 0

t_0 = ScannersAtTime(firewall, 0)
print (sum(t_0))

while True:
    if IsOpen(firewall, delta):
        break
    delta += 1
    
print delta