# -*- coding: utf-8 -*-

def GetMemHash(memory):
    mem_hash = "-".join([str(m) for m in memory])
    return mem_hash

def FindMax(memory):
    max_el = max(memory)
    return (max_el, memory.index(max_el))

input_file = 'aoc06-input.txt'

banks = []

with open(input_file, 'r') as f:
    banks = f.readlines()

banks = [b.replace("\n", "").replace("\r", "") for b in banks]

memory = [int(b) for b in banks[0].split("\t")]

mem_hash = GetMemHash(memory)
mem_hashes = [mem_hash]

while True:
    (max_el, max_i) = FindMax(memory)
    memory[max_i] = 0
    for i in range(max_i + 1, max_i + 1 + max_el):
        m_i = i % len(memory)
        memory[m_i] += 1
    mem_hash = GetMemHash(memory)
    
    if mem_hash in mem_hashes:
        break
    else:
        mem_hashes.append(mem_hash)

print len(mem_hashes)
print mem_hashes.index(mem_hash)
print len(mem_hashes) - mem_hashes.index(mem_hash)