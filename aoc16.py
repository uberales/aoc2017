# -*- coding: utf-8 -*-

def main():

    input_file = 'aoc16-input.txt'

    dance = []

    letters = list('abcdefghijklmnop')

    with open(input_file, 'r') as f:
        dance = f.readline().strip().split(',')

    for i in range(1000000000):
        for m in dance:
            if m[0] == 's':
                num = int(m[1:])
                start = letters[0:len(letters) - num]
                ending = letters[-num:]
                ending.extend(start)
                letters = ending
            elif m[0] == 'x':
                a = int(m[1:].split('/')[0])
                b = int(m[1:].split('/')[1])
                p_a = letters[a]
                letters[a] = letters[b]
                letters[b] = p_a
            elif m[0] == 'p':
                p_a = m[1:].split('/')[0]
                p_b = m[1:].split('/')[1]
                i_a = letters.index(p_a)
                i_b = letters.index(p_b)
                letters[i_a] = p_b
                letters[i_b] = p_a

        if i % 10000 == 0:
            print i, ''.join(letters)

    print ''.join(letters)
if __name__ == "__main__":
    main()
