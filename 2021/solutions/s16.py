with open('../inputs/input16.txt') as f:
    f = f.read().splitlines()[0]
f_bin = ''.join([bin(int(s, 16))[2:].zfill(4) for s in f])

def literal_packet(s):
    p_version, p_type = int(s[0:3],2), int(s[3:6], 2)
    flag = s[6]
    group = s[7:11]
    start = 6
    while flag=='1':
        start += 5
        flag = s[start]
        group += s[start+1:start+5]
    packet = int(group, 2)
    s = s[start+5:]
    return (p_version, p_type, packet, s)

def op0_packet(s):
    p_version, p_type = int(s[0:3],2), int(s[3:6], 2)
    subpacket = s[22:]
    return p_version, p_type, subpacket

def op1_packet(s):
    p_version, p_type = int(s[0:3],2), int(s[3:6], 2)
    subpacket = s[18:]
    return p_version, p_type, subpacket

def unpack(s1):
    list_packet = []

    while len(s1)>0:
        if int(s1[3:6],2) == 4:
            _ver, _type, _value, s1 = literal_packet(s1)
            list_packet.append((_ver, _type, _value))    
        else:
            if s1[6]=='0':
                _ver, _type, s1 = op0_packet(s1)
                list_packet.append((_ver, _type))
            else:
                _ver, _type, s1 = op1_packet(s1)
                list_packet.append((_ver, _type))
        if len(s1)==0 or int(s1, 2)==0:
            break
    return list_packet

unpacked = unpack(f_bin)
print('Part 1:', sum([l[0] for l in unpacked]))

dict_operation = {'0':'+', '1':'*', '2':'min', '3':'max', '5':'gt', '6':'lt', '7':'eq'}
expression = ','.join([str(l[2]) if l[1]==4 else dict_operation[str(l[1])] for l in unpacked])
print(expression)

from functools import reduce

def calcs(exp0):
    if exp0[0] == '+':
        return sum([int(i) for i in exp0[1:]])
    if exp0[0] == '*':
        return reduce(lambda x, y: x*y, [int(i) for i in exp0[1:]])
    if exp0[0] == 'min':
        return min([int(i) for i in exp0[1:]])
    if exp0[0] == 'max':
        return max([int(i) for i in exp0[1:]])
    if exp0[0] == 'lt':
        return int(int(exp0[1])<int(exp0[2]))
    if exp0[0] == 'gt':
        return int(int(exp0[1])>int(exp0[2]))
    if exp0[0] == 'eq':
        return int(int(exp0[1])==int(exp0[2]))

# online solution for part 2
import math

op = [sum, math.prod, min, max,
      lambda ls: ls[0], # literal
      lambda ls: 1 if ls[0] > ls[1] else 0,  # gt
      lambda ls: 1 if ls[0] < ls[1] else 0,  # lt
      lambda ls: 1 if ls[0] == ls[1] else 0] # eq

bs = f_bin

def ps2(startbit):
    i = startbit # index into bs
    ID = int(bs[i+3:i+6],2) # packet type ID
    i += 6
    if ID == 4: #literal value
        vals = [0]
        while True:
            vals[0] = 16*vals[0] + int(bs[i+1:i+5],2)
            i += 5
            if bs[i-5] == '0': #last value packet
                break
    else:
        vals = []
        if bs[i] == '0': # subpacket length in bits
            endi = i + 16 + int(bs[i+1:i+16],2)
            i += 16
            while i < endi:
                i,v = ps2(i)
                vals.append(v)
        else:
            np = int(bs[i+1:i+12],2) # number of subpackets
            i += 12
            for _ in range(np):
                i,v = ps2(i)
                vals.append(v)

    return i,op[ID](vals)

print('part 2: ', ps2(0)[1])