# -*- coding: utf-8 -*-

def Avail(plug, taken):
    return plug[0] if plug[1] == taken else plug[1]

def GetCompatible(pin, plugs, taken):
    compatibles = []
    for plug in plugs:
        if pin in plug and not plug in taken:
            compatibles.append(plug)
    return compatibles

def Strength(chain):
    s = 0
    for l in chain:
        s += l[0] + l[1]
    #print '-'.join([str(l) for l in chain])
    return s

def Append(chain, pin, plugs, chain_record):
    compatibles =  GetCompatible(pin, plugs, chain)
    #print chain, pin
    if len(compatibles) > 0:
        for c in compatibles:
            new_chain = list(chain)
            new_chain.append(c)
            new_pin = Avail(c, pin)
            Append(new_chain, new_pin, plugs, chain_record)
    else:
        s = Strength(chain)
        chain_record.append((s, len(chain), chain))

def main():
    input_file = 'aoc24-input.txt'
    plugs = []

    with open(input_file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            data = l.split('/')
            plug = (int(data[0]), int(data[1]))
            plugs.append(plug)

    print len(plugs)
    print len(set(plugs))

    chain_record = []
    Append([], 0, plugs, chain_record)

    chain_record.sort(key=lambda c:(c[0]))
    print chain_record[-1]

    chain_record.sort(key=lambda c:(c[1], c[0]))
    print chain_record[-1]



if __name__ == "__main__":
    main()
