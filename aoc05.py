# -*- coding: utf-8 -*-

input_file = 'aoc05-input.txt'

lines = []

with open(input_file, 'r') as f:
    lines = f.readlines()

jumps = [int(l.replace("\n", "").replace("\r", "")) for l in lines]

jump_i = 0
iterations = 0

while jump_i >= 0 and jump_i < len(jumps):
    jump_delta = jumps[jump_i]
    jumps[jump_i] += 1
    jump_i += jump_delta
    iterations += 1

print iterations
    

input_file = 'aoc05-input.txt'

lines = []

with open(input_file, 'r') as f:
    lines = f.readlines()

jumps = [int(l.replace("\n", "").replace("\r", "")) for l in lines]

jump_i = 0
iterations = 0

while jump_i >= 0 and jump_i < len(jumps):
    jump_delta = jumps[jump_i]
    if jumps[jump_i] >= 3:
        jumps[jump_i] += -1
    else:
        jumps[jump_i]+= 1
    jump_i += jump_delta
    iterations += 1

print iterations
    
