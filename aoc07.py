# -*- coding: utf-8 -*-

import re
input_file = 'aoc07-input.txt'

# global :P
programs = {}

with open(input_file, 'r') as f:
    for l in f.readlines():
        l = l.strip()
        m = re.search('([a-z]*) \(([0-9]*)\)[ ->]*(.*)', l)
        g = m.groups()
        
        program = {
            "name": g[0],
            "weight": int(g[1]),
            "links": g[2].split(", ") if len(g[2]) > 0 else []
        }
        
        programs[program["name"]] = program

# find any (first) leaf node
pivot = [programs[k] for k in programs if len(programs[k]["links"]) == 0][0]

# find root node (backwards search)
while True:
    found = False
    for n in programs:
        p = programs[n]
        if pivot["name"] in p["links"]:
            pivot = p
            found = True
            break
    if not found:
        break

print "root node: ", pivot["name"]

# recursive weighting
# no cycles assumed
def WeightNode(node):
    weight = node["weight"]
    for l in node["links"]:
        weight += WeightNode(programs[l])
    return weight

# find the unballanced node from a node list of another node
def GetUnballancedNode(node, is_heavier):
    weights = []
    
    for l in node["links"]:
        weights.append((WeightNode(programs[l]), l))
    max_w = max(weights)
    min_w = min(weights)
        
    # either this node is unballanced itself
    if max_w[0] == min_w[0]:
        return node
    # or there is an unballanced tower on the node
    elif is_heavier:
        return programs[max_w[1]]
    else:
        return programs[min_w[1]]

# we expect that exactly one node is unballanced and there is no weirdness in the graph (eg. cycles)
# find whether the wrong node is heavier
weights = []    
for l in pivot["links"]:
    weights.append((WeightNode(programs[l]), l))

min_node = programs[min(weights)[1]]
# at the moment, it is not necessary to know the result (hence False as is_heavier parameter)
is_heavier = False
min_unballanced = GetUnballancedNode(min_node, is_heavier)
delta = max(weights)[0] - min(weights)[0]

if min_unballanced["name"] == min_node["name"]:
    is_heavier = True
    delta = - delta
    print "Unballanced is heavier"
else:
    print "Unballanced is lighter"

while True:
    prev_name = pivot["name"]

    pivot = GetUnballancedNode(pivot, is_heavier)
    
    if pivot["name"] == prev_name:
        break
    
    if len(pivot["links"]) == 0:
        break
        
print pivot

correct_weight = pivot["weight"] + delta

print correct_weight
    