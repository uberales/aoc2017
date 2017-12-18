# -*- coding: utf-8 -*-
import time

def IsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        pass
    return False

def Beep(frequency):
    # beep
    return frequency
    
def GetValue(registers, index_or_value):
    val = index_or_value
    if not IsInt(val):
        if index_or_value in registers:
            val = registers[index_or_value]
        else:
            registers[index_or_value] = long(0)
            return long(0)
    return val
    

def Play(instructions):
    registers = {}
    current_pos = 0
    last_sound = -1
    while True:
        instruction = instructions[current_pos]
        current_pos += 1
        code = instruction[0]
        
        if code == 'snd':
            last_sound = Beep(GetValue(registers, instruction[1]))
        elif code == 'set':
            val = GetValue(registers, instruction[2])
            if not instruction[1] in registers: registers[instruction[1]] = 0
            registers[instruction[1]] = val
        elif code == 'add':
            val = GetValue(registers, instruction[2])
            if not instruction[1] in registers: registers[instruction[1]] = 0
            registers[instruction[1]] += val
        elif code == 'mul':
            val = GetValue(registers, instruction[2])
            if not instruction[1] in registers: registers[instruction[1]] = 0
            registers[instruction[1]] = registers[instruction[1]] * val
        elif code == 'mod':
            val = GetValue(registers, instruction[2])
            if not instruction[1] in registers: registers[instruction[1]] = 0
            registers[instruction[1]] = registers[instruction[1]] % val
        elif code == 'rcv':
            val = GetValue(registers, instruction[1])
            if val != 0:
                break
        elif code == 'jgz':
            val_x = GetValue(registers, instruction[1])
            val_y = GetValue(registers, instruction[2])
            if val_x > 0:
                current_pos += val_y - 1
        
            
    return last_sound

def Step(p_id, instructions, registers, current_pos, send_cnt, buffer_in, buffer_out):
    instruction = instructions[current_pos]
    
    code = instruction[0]
    print "\t".join([str(e) for e in [p_id, instruction, registers, current_pos]])

    current_pos += 1
    waiting = False
    

    if code == 'snd':
        buffer_out.append(GetValue(registers, instruction[1]))
        send_cnt += 1
    elif code == 'set':
        val = GetValue(registers, instruction[2])
        if not instruction[1] in registers: registers[instruction[1]] = long(0)
        registers[instruction[1]] = val
    elif code == 'add':
        val = GetValue(registers, instruction[2])
        if not instruction[1] in registers: registers[instruction[1]] = long(0)
        registers[instruction[1]] += val
    elif code == 'mul':
        val = GetValue(registers, instruction[2])
        if not instruction[1] in registers: registers[instruction[1]] = long(0)
        registers[instruction[1]] = registers[instruction[1]] * val
    elif code == 'mod':
        val = GetValue(registers, instruction[2])
        if not instruction[1] in registers: registers[instruction[1]] = long(0)
        registers[instruction[1]] = registers[instruction[1]] % val
    elif code == 'rcv':
        if len(buffer_in) == 0:
            current_pos -= 1
            waiting = True
        else:
            if not instruction[1] in registers: registers[instruction[1]] = long(0)
            registers[instruction[1]] = buffer_in.pop(0)
        
    elif code == 'jgz':
        val_x = GetValue(registers, instruction[1])
        val_y = GetValue(registers, instruction[2])
        if val_x > 0:
            current_pos += val_y - 1
            
    if current_pos < 0 or current_pos >= len(instructions):
        print "Terminated by jumping out"
        waiting = True
        
    return (current_pos, send_cnt, waiting)

def Communicate(instructions):
    registers_a = {"p": 0}
    registers_b = {"p": 1}
    current_pos_a = 0
    current_pos_b = 0
    buffer_in = []
    buffer_out = []
    send_cnt_a = 0

    i = 0
    while True:
        step_a = Step("a", instructions, registers_a, current_pos_a, send_cnt_a, buffer_in, buffer_out)
        step_b = Step("b", instructions, registers_b, current_pos_b, 0, buffer_out, buffer_in)
        
        if step_a[2] and step_b[2]:
            return step_a[1]
        
        current_pos_a = step_a[0]
        current_pos_b = step_b[0]
        
        send_cnt_a = step_a[1]
        
        i += 1
        print

def main():
    input_file = 'aoc18-input.txt'
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
    
    print instructions
    print len(instructions)
    
    task_a = Play(instructions)
    print task_a
    
    task_b = Communicate(instructions)  
    print task_b
    

if __name__ == "__main__":
    main()
