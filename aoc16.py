# -*- coding: utf-8 -*-

def Dance(letters, dance):
    new_letters = [l for l in letters]
    for m in dance:
        if m[0] == 's':
            num = int(m[1:])
            start = new_letters[0:len(new_letters) - num]
            ending = new_letters[-num:]
            ending.extend(start)
            new_letters = ending
        elif m[0] == 'x':
            a = int(m[1:].split('/')[0])
            b = int(m[1:].split('/')[1])
            p_a = new_letters[a]
            new_letters[a] = new_letters[b]
            new_letters[b] = p_a
        elif m[0] == 'p':
            p_a = m[1:].split('/')[0]
            p_b = m[1:].split('/')[1]
            i_a = new_letters.index(p_a)
            i_b = new_letters.index(p_b)
            new_letters[i_a] = p_b
            new_letters[i_b] = p_a
    return new_letters

def main():

    input_file = 'aoc16-input.txt'

    dance = []

    str = 'abcdefghijklmnop'
    letters = list('abcdefghijklmnop')

    with open(input_file, 'r') as f:
        dance = f.readline().strip().split(',')

    letters_1 = Dance(letters, dance)

    print ''.join(letters_1)
    period = 0
    while True:
        letters = Dance(letters, dance)
        period += 1
        this_str = ''.join(letters)
        if this_str == str:
            break
    print period

    total_count = 1000000000
    restricted = total_count % period

    for i in range(restricted):
        letters = Dance(letters, dance)
    print ''.join(letters)

if __name__ == "__main__":
    main()
