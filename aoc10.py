# -*- coding: utf-8 -*-

def Hash1(knot, tie_lengths):
    jump_delta = 0
    knot_start = 0    
    knot_len = len(knot)

    
    for tie in tie_lengths:
    
        if knot_start + tie > knot_len:
            part_len = knot_start + tie - knot_len
            sub_list = knot[knot_start:]
            sub_list.extend(knot[0:part_len])
            sub_list.reverse()
            knot[knot_start:] = sub_list[0:tie - part_len]
            knot[0:part_len] = sub_list[tie - part_len:]
        else:
            sub_list = knot[knot_start:knot_start+tie]
            sub_list.reverse()
            knot[knot_start:knot_start + tie] = sub_list[0:]
    
        knot_start = (knot_start + jump_delta + tie) % knot_len
        jump_delta += 1
    
    return knot
    
def Hash2(knot, tie_lengths):
    jump_delta = 0
    knot_start = 0
    knot_len = len(knot)
    
    for i in range(64):
        for tie in tie_lengths:
            if knot_start + tie > knot_len:
                part_len = knot_start + tie - knot_len
                sub_list = knot[knot_start:]
                sub_list.extend(knot[0:part_len])
                sub_list.reverse()
                knot[knot_start:] = sub_list[0:tie - part_len]
                knot[0:part_len] = sub_list[tie - part_len:]
            else:
                sub_list = knot[knot_start:knot_start+tie]
                sub_list.reverse()
                knot[knot_start:knot_start + tie] = sub_list[0:]
        
            knot_start = (knot_start + jump_delta + tie) % knot_len
            jump_delta += 1
    
    hashed = ""
    for i in range(0, 256, 16):
        sub_knot = knot[i:i + 16]
        b = 0
        for k in sub_knot:
            b = b ^ k
        hashed += '{:02x}'.format(b)
    return hashed


def KnotHash(string):
    tie_lengths = [ord(c) for c in list(string)]
    tie_lengths.extend([17, 31, 73, 47, 23])
    knot_len = 256
    knot = range(knot_len)

    return Hash2(knot, tie_lengths)


def main():
    
    input_file = 'aoc10-input.txt'
    knot_len = 256
    knot = range(knot_len)
    
    tie_lengths = []
    
    with open(input_file, mode="r") as f:
        tie_lengths = [int(i) for i in f.read().strip().split(',')]
    
    
    knot = Hash1(knot, tie_lengths)
    
    print knot[0]*knot[1]

    
    with open(input_file, mode="r") as f:
        string = f.read().strip()
    
    print string
    print KnotHash(string)

if __name__ == "__main__":
    main()
