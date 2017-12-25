# -*- coding: utf-8 -*-

def Get(tape, i):
    if not i in tape:
        tape[i] = 0
    return tape[i]

def Machine(tape, steps):
    c = 0
    state = 'a'
    position = 0
    while c < steps:
        c += 1
        val = Get(tape, position)
        delta = 0

        if state == 'a':
            if val == 0:
                tape[position] = 1
                delta = 1
                state = 'b'
            elif val == 1:
                tape[position] = 0
                delta = 1
                state = 'f'
        elif state == 'b':
            if val == 0:
                tape[position] = 0
                delta = -1
                state = 'b'
            elif val == 1:
                tape[position] = 1
                delta = -1
                state = 'c'
        elif state == 'c':
            if val == 0:
                tape[position] = 1
                delta = -1
                state = 'd'
            elif val == 1:
                tape[position] = 0
                delta = 1
                state = 'c'
        elif state == 'd':
            if val == 0:
                tape[position] = 1
                delta = -1
                state = 'e'
            elif val == 1:
                tape[position] = 1
                delta = 1
                state = 'a'
        elif state == 'e':
            if val == 0:
                tape[position] = 1
                delta = -1
                state = 'f'
            elif val == 1:
                tape[position] = 0
                delta = -1
                state = 'd'
        elif state == 'f':
            if val == 0:
                tape[position] = 1
                delta = 1
                state = 'a'
            elif val == 1:
                tape[position] = 0
                delta = -1
                state = 'e'

        position += delta


def main():
    steps = 12425180
    tape = {}

    Machine(tape, steps)

    checksum = sum(tape.itervalues())
    print checksum

if __name__ == "__main__":
    main()
