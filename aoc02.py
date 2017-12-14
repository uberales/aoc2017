# -*- coding: utf-8 -*-

input_file = 'aoc02-input.text'

lines = []

with open(input_file, 'r') as f:
    lines = f.readlines()

lines = [l.replace("\r", "") for l in lines]
sheet = []

for l in lines:
    sheet.append([int(c) for c in l.split("\t")])

checksum = 0
checksum_2 = 0
for row in sheet:
    r_min = min(row)
    r_max = max(row)
    
    delta = r_max - r_min
    checksum += delta
        
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            vals = [row[i], row[j]]
            c_min = min(vals)
            c_max = max(vals)
            if c_max % c_min == 0:
                checksum_2 += c_max / c_min

print checksum
print checksum_2
