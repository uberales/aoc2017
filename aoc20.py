# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 09:46:40 2017

@author: podolnik
"""

import re
import numpy as np

def Move(particles):
    for p in particles:
        p["v"] = p["v"] + p["a"]
        p["p"] = p["p"] + p["v"]
        p["d"] = sum([abs(n) for n in p["p"]])
    particles.sort(key=lambda p: p["d"])

def Collide(particles):
    positions = [(tuple(p["p"])) for p in particles]
    multiples = set()
    all_pos = set()
    
    for p in positions:
        if p in all_pos:
            multiples.add(p)
        all_pos.add(p)
        
    new_particles = []
    for p in particles:
        position = tuple(p["p"])
        if not position in multiples:
            new_particles.append(p)
        
    return new_particles
        
def main():
    input_file = 'aoc20-input.txt'
    
    particles = []
    
    with open(input_file, 'r') as f:
       lines = ''.join(f.read())
       matches = re.findall("p=<([-0-9]*),([-0-9]*),([-0-9]*)>, v=<([-0-9]*),([-0-9]*),([-0-9]*)>, a=<([-0-9]*),([-0-9]*),([-0-9]*)>", lines)
       i = 0
       for m in matches: 
           p = {
               "p": np.array([int(n) for n in m[0:3]]),
               "v": np.array([int(n) for n in m[3:6]]),
               "a": np.array([int(n) for n in m[6:9]]),
               "d": sum([abs(int(n)) for n in m[0:3]]),
               "i": i
           }
           particles.append(p)
           i += 1

    particles.sort(key = lambda p: sum([abs(n) for n in p["a"]]))
    print 'closest:', particles[0]["i"]

    for i in range(1000):
        Move(particles)
        particles = Collide(particles)
    
    print 'after 1000 steps:', len(particles)
        
if __name__ == "__main__":
    main()
