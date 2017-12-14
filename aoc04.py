# -*- coding: utf-8 -*-

input_file = 'aoc04-input.txt'

lines = []

with open(input_file, 'r') as f:
    lines = f.readlines()

lines = [l.replace("\n", "").replace("\r", "") for l in lines]

valid = 0

for line in lines:
    words = line.split(' ')
    word_set = set(words)
    if len(words) == len(word_set):
        valid += 1

print valid

valid = 0

for line in lines:
    words = [''.join(sorted(w)) for w in line.split(' ')]
    word_set = set(words)
    if len(words) == len(word_set):
        valid += 1

print valid