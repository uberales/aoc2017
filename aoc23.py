# -*- coding: utf-8 -*-
import numpy as np


def IsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        pass
    return False

def GetValue(registers, index_or_value):
    val = index_or_value
    if not IsInt(val):
        if index_or_value in registers:
            val = registers[index_or_value]
        else:
            registers[index_or_value] = long(0)
            return long(0)
    return val


def ShowH(registers, instruction):
    if instruction == 'h':
        print registers[instruction]


def Play(registers, instructions):
    current_pos = 0

    mul_times = 0
    while True:
        instruction = instructions[current_pos]
        current_pos += 1
        code = instruction[0]

        if code == 'snd':
            pass
        elif code == 'set':
            val = GetValue(registers, instruction[2])
            registers[instruction[1]] = val
            ShowH(registers, instruction[1])
        elif code == 'sub':
            val = GetValue(registers, instruction[2])
            registers[instruction[1]] -= val
            ShowH(registers, instruction[1])
        elif code == 'mul':
            val = GetValue(registers, instruction[2])
            registers[instruction[1]] = registers[instruction[1]] * val
            mul_times += 1
            ShowH(registers, instruction[1])
        elif code == 'jnz':
            val_x = GetValue(registers, instruction[1])
            val_y = GetValue(registers, instruction[2])
            if not val_x == 0:
                current_pos += val_y - 1

        if current_pos < 0 or current_pos >= len(instructions):
            break

    return mul_times

def IsPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, int(np.sqrt(n))):
            if n % x == 0:
                return False
        return True

def Machine():
    h = 0

    for b in range(108400, 125400 + 1, 17):
        if not IsPrime(b):
            h += 1

    print 'done', h


def main():
    input_file = 'aoc23-input.txt'
    instructions = []

    with open(input_file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip().split(' ')
            i = None
            if len(l) == 3:
                i = (l[0], int(l[1]) if IsInt(l[1]) else l[1], int(l[2]) if IsInt(l[2]) else l[2])
            else:
                i = (l[0], int(l[1]) if IsInt(l[1]) else l[1])
            instructions.append(i)

    registers = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}

    task_a = Play(registers, instructions)
    print task_a

    Machine()

if __name__ == "__main__":
    main()
