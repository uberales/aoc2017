# -*- coding: utf-8 -*-

from aoc10 import KnotHash

def Hash2Bin(s):
    s = ''.join([format(int(c, 16), '04b') for c in list(s)])
    return [int(i) for i in list(s)]

def Paint(bank, r, c, q, r_dim, c_dim):
    if r >= 0 and r < r_dim and c >= 0 and c < c_dim:
        if bank[r][c] == -1:
            bank[r][c] = q
            Paint(bank, r - 1, c, q, r_dim, c_dim)
            Paint(bank, r + 1, c, q, r_dim, c_dim)
            Paint(bank, r, c - 1, q, r_dim, c_dim)
            Paint(bank, r, c + 1, q, r_dim, c_dim)

def main():
    
    input_str = 'uugsqrei'
    
    used = 0
    bank = []
    for i in range(128):
        row = input_str + '-' + str(i)
        row_hash = KnotHash(row)
        row_bin = Hash2Bin(row_hash)
        used += sum(row_bin)
        bank.append([-i for i in row_bin])
    
    print used
    
    r_dim = len(bank)
    c_dim = len(bank[0])
    
    q = 0
    for r in range(r_dim):
        for c in range(c_dim):
            if bank[r][c] == -1:
                q = q + 1
                Paint(bank, r, c, q, r_dim, c_dim)
    
    print q

if __name__ == "__main__":
    main()
