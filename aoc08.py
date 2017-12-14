# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:47:36 2017

@author: podolnik
"""

import re
input_file = 'aoc08-input.txt'

instructions = []
registers = {}

with open(input_file, 'r') as f:
    for l in f.readlines():
        l = l.strip()
        m = re.match("([a-z]*) ([a-z]*) ([-0-9]*) if ([a-z]*) (.*) ([-0-9]*)", l)
        
        register = m.group(1)
        operator = "-" if m.group(2) == "dec" else "+"
        value = int(m.group(3))
        decision = m.group(4)
        comparator = m.group(5)
        needle = int(m.group(6))
        
        registers[register] = 0
        instruction = 'registers["{0}"] = registers["{0}"] {1} {2} if registers["{3}"] {4} {5} else registers["{0}"]'.format(register, operator, value, decision, comparator, needle)
        
        instructions.append((register, instruction))

pass

max_val = 0
current = 0

for ins_def in instructions:
    
    reg = ins_def[0]
    ins = ins_def[1]
    
    print ins
    exec(ins)
    
    if registers[reg] > max_val:
        max_val = registers[reg]
    
print max(registers.itervalues())
print max_val