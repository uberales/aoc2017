# -*- coding: utf-8 -*-

import re
input_file = 'aoc09-input.txt'

stream = []

with open(input_file, 'r') as f:
    line = f.readline().strip()
#    line = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
    stream = list(line)

print len(stream)

stream_ignored = []

i = 0
while i < len(stream):
    c = stream[i]
    if c == '!':
        i += 1
    else:
        stream_ignored.append(c)
        
    i += 1

print 'after ignore', len(stream_ignored)

stream_purged = []

i = 0
reading = True
purged = 0

while i < len(stream_ignored):
    c = stream_ignored[i]
    if reading and c == '<':
        reading = False
    elif reading:
        stream_purged.append(c)
    elif c == '>':
        reading = True
    else:
        purged += 1
    i += 1


print 'after purge',len(stream_purged)
print 'purged', purged

score = 0
total = 0

for c in stream_purged:
    if c == '{':
        score += 1
    elif c == '}':
        total += score
        score += -1

print 'scoring',total
