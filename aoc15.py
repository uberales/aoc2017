# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:00:23 2017

@author: podolnik
"""

def Generator(factor, previous):
    n = (previous * factor) % 2147483647
    return n
    
def ModGenerator(factor, previous, modulus):
    while True:
        previous = (previous * factor) % 2147483647
        if previous % modulus == 0:
            return previous

def main():
    factor_a = 16807
    factor_b = 48271
    
    starting_a = 873
    starting_b = 583
    
#    prev_a = 65
#    prev_b = 8921
    prev_a = starting_a
    prev_b = starting_b
    
    judge = 65536
    
    matches = 0
    
    print 'task 1'
    
    for i in range(40000000):
        prev_a = Generator(factor_a, prev_a)
        prev_b = Generator(factor_b, prev_b)
        result = (prev_b - prev_a) % judge
        if result == 0:
            matches += 1
    
    print matches
    
    print 'task 2'
    
    matches = 0
    
    modulus_a = 4
    modulus_b = 8
    prev_a = starting_a
    prev_b = starting_b
    for i in range(5000000):
        prev_a = ModGenerator(factor_a, prev_a, modulus_a)
        prev_b = ModGenerator(factor_b, prev_b, modulus_b)
        result = (prev_b - prev_a) % judge
        if result == 0:
            matches += 1

    print matches
        
if __name__ == "__main__":
    main()
