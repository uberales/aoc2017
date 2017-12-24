# -*- coding: utf-8 -*-
import time


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

def EqualHistories(h_a, h_b):
    if len(h_a) == len(h_b):
        for i in range(len(h_a)):
            if h_a[i][0] != h_b[i][0]:
                return False
        return True
    return False

def CheckPeriodicity(total_record, delta, period):
    h_a = total_record[-delta]
    h_b = total_record[-delta - period]
    return EqualHistories(h_a, h_b)

def GetHistoryPeriod(total_record, max_period):
    period = 0
    for p in range(1, max_period + 1):
        is_periodic = True
        for delta in range(1, p + 1):
            is_periodic = CheckPeriodicity(total_record, delta, p)
            if not is_periodic: break
        if is_periodic:
            period = p
            break
    return period

def Substract(reg_a, reg_b):
    differences = {}
    for k in reg_a:
        differences[k] = reg_a[k] - reg_b[k]
    return differences

def PredictLength(h_this, h_prev):
    reg_this = h_this[2]
    reg_prev = h_prev[2]
    pivot_r = h_this[1][1]

    differences = Substract(reg_this, reg_prev)
    if abs(reg_this[pivot_r] - 0) < abs(reg_prev[pivot_r]):

        pivot_d = differences[pivot_r]
        remaining = abs(reg_this[pivot_r])
        if remaining % pivot_d == 0:
            count = remaining / pivot_d
            return count

    return -1

def CheckHistory(total_record, history):

    result = (0, {})
    max_period = 2

    total_record.append(history)

    if len(total_record) > 2 * max_period:
        repeat_period = GetHistoryPeriod(total_record, max_period)
        if repeat_period > 0:
            min_period = -1
            period_data = []
            for s_p in range(1,repeat_period + 1):
                this_ins = total_record[-s_p][-1]
                prev_ins = total_record[-s_p - repeat_period][-1]
                predicted = PredictLength(this_ins, prev_ins)
                if predicted > 0:
                    period_data.append((s_p, predicted))

            if len(period_data) > 0:
                period_data.sort(key=lambda pd: pd[0])
                offset = period_data[0][0]
                repetitions = period_data[0][1]

                #print period_data[0]
                #print 'jumping from', total_record[-offset][-1]

                this_reg = total_record[-offset][-1][2]
                prev_reg = total_record[-offset - repeat_period][-1][2]
                instruction = total_record[-offset][-1][1]
                position = total_record[-offset][-1][0]
                differences = Substract(this_reg, prev_reg)
                next_reg = this_reg.copy()
                for k in next_reg:
                    next_reg[k] += differences[k] * repetitions
                result = (repetitions, next_reg, position, instruction)


    return result

def Play2(registers, instructions):
    current_pos = 0

    mul_times = 0

    total_record = []
    history = []

    count = 0

    while True:
        instruction = instructions[current_pos]

        #print (current_pos, instruction, registers)
        history.append((current_pos, instruction, registers.copy()))
#        history.append((current_pos))

        current_pos += 1
        code = instruction[0]

        if code == 'set':
            val = GetValue(registers, instruction[2])
            registers[instruction[1]] = val
        elif code == 'sub':
            val = GetValue(registers, instruction[2])
            registers[instruction[1]] -= val
            #if instruction[1] == 'b':
            #    print current_pos, registers
        elif code == 'mul':
            val = GetValue(registers, instruction[2])
            registers[instruction[1]] = registers[instruction[1]] * val
            mul_times += 1
        elif code == 'jnz':

            skip_params = CheckHistory(total_record, history)

            if not skip_params[0] == 0:
                for r in registers:
                    registers[r] = skip_params[1][r]
                instruction = skip_params[3]
                current_pos = skip_params[2] + 1

                #print 'skipped', skip_params[0]
                #print 'jumping to', (current_pos, instruction, registers.copy())
                #total_record.append([(current_pos, instruction, registers.copy())])
            history = []

            val_x = GetValue(registers, instruction[1])
            val_y = GetValue(registers, instruction[2])
            if not val_x == 0:
                current_pos += val_y - 1

        if current_pos < 0 or current_pos >= len(instructions):
            break

        if count % 1000000 == 0:
            print count, registers

        count += 1

    print count
    return mul_times


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

    #task_a = Play(registers, instructions)
    #print task_a

    registers = {"a": 1, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}

    #registers = {"a": 1, "b": 125400, "c": 125400, "d": 125383, "e": 125383, "f": 0, "g": -17, "h": 1000}

    task_b = Play2(registers, instructions)
    print task_b, registers

if __name__ == "__main__":
    main()
