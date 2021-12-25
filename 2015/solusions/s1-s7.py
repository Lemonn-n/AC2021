#!/usr/bin/env python
# coding: utf-8

# ### Day1

f = open('./2015/inputs/input1.txt').read()

floor = 0
for fi in f:
    if fi == '(': floor += 1
    else: floor -= 1
print('part1: ', floor)

floor = 0
for i,fi in enumerate(f):
    if fi == '(': floor += 1
    else: floor -= 1
    if floor == -1:
        print('part2: ', i+1)
        break


# ### Day2

f = open('./2015/inputs/input2.txt').read().splitlines()
f = [fi.split('x') for fi in f]
f = [[int(fii) for fii in fi] for fi in f]

paper = 0
ribbon = 0
for fi in f:
    dim = sorted(fi)
    paper += 3*dim[0]*dim[1]+2*dim[1]*dim[2]+2*dim[0]*dim[2]
    ribbon += 2*dim[0]+2*dim[1]+dim[0]*dim[1]*dim[2]
print('part1: ', paper)
print('part2: ', ribbon)


# ### Day3

f = open('./2015/inputs/input3.txt').read()

from collections import defaultdict

def deliver(path):
    house = defaultdict(int)
    house[(0,0)] = 1
    i = 0
    j = 0
    for fi in path:
        if fi == '^':
            j += 1
        if fi == 'v':
            j -= 1
        if fi == '<':
            i -= 1
        if fi == '>':
            i += 1
        house[(i,j)]+=1
    return house

house = deliver(f)
print('part1: ', len([k for k,v in house.items() if v>=1]))

path1, path2 = f[::2], f[1::2]
house1, house2 = deliver(path1), deliver(path2)
add1 = [k for k,v in house1.items() if v>=1]
add2 = [k for k,v in house2.items() if v>=1]
print('part2: ', len(set(add1) | set(add2)))


# ### Day4

import hashlib

start = 'iwrupvqb'

i = 1
while True:
    st = start+str(i)
    if hashlib.md5(st.encode('utf-8')).hexdigest()[:5] == '00000':
        print('part1: ', i)
        break
    i += 1

    
# Multi-threading solution

import threading

def multi_find(threads, maxN):
    def find(start, searchRange):
        for i in searchRange:
            st = start+str(i)
            if hashlib.md5(st.encode('utf-8')).hexdigest()[:6] == '000000':
                print(i,'\n')
                break
    for thread in range(threads):
        r = range(1+thread, maxN+thread, threads)
        t = threading.Thread(target=find, args=(start, r))
        t.start()
        t.join()

print('part2: ', multi_find(10, 10**7))

# itertool solution - not sure why but it's much faster than part1 counting

import itertools

for i in itertools.count():
    if hashlib.md5((start+str(i)).encode('utf-8')).hexdigest()[:6] == '000000':
        print('part2 alternative: ', i)
        break


# ### Day5

f = open('./2015/inputs/input5.txt').read().splitlines()

def nice_cnt(f):
    nice_cnt = 0
    for fi in f:
        c1 = fi.count('a')+fi.count('e')+fi.count('i')+fi.count('o')+fi.count('u') >= 3
        c2 = any([fi[i]==fi[i-1] for i in range(1, len(fi))])
        c3 = fi.count('ab')+fi.count('cd')+fi.count('pq')+fi.count('xy')==0
        if c1 and c2 and c3:
            nice_cnt += 1
    return nice_cnt
print('part1: ', nice_cnt(f))

def nice_cnt2(f):
    nice_cnt = 0
    for fi in f:
        c1 = any([any([fi[i:i+2]==fi[j:j+2] for j in range(i+2, len(fi)-1)]) for i in range(len(fi)-1)])
        c2 = any([fi[i]==fi[i-2] for i in range(2, len(fi))])
        if c1 and c2:
            nice_cnt += 1
    return nice_cnt
print('part2: ', nice_cnt2(f))


# ### Day6

f = open('./2015/inputs/input6.txt').read().splitlines()
f = [fi.split(' ') for fi in f]
f = [fi if len(fi)==4 else fi[1:] for fi in f]
f = [(fi[0], tuple([int(fii) for fii in fi[1].split(',')]),      tuple([int(fii) for fii in fi[3].split(',')])) for fi in f]

import numpy as np

window = np.zeros((1000, 1000))
for fi in f:
    flag, start, end = fi
    ymin, ymax = start[0], end[0]
    xmin, xmax = start[1], end[1]
    if flag == 'on':
        window[xmin:xmax+1, ymin:ymax+1]=1
    elif flag == 'off':
        window[xmin:xmax+1, ymin:ymax+1]=0
    elif flag == 'toggle':
        window[xmin:xmax+1, ymin:ymax+1]=1-window[xmin:xmax+1, ymin:ymax+1]
print('part1: ', (window==1).sum().sum()) 

window = np.zeros((1000, 1000))
for fi in f:
    flag, start, end = fi
    ymin, ymax = start[0], end[0]
    xmin, xmax = start[1], end[1]
    if flag == 'on':
        window[xmin:xmax+1, ymin:ymax+1]+=1
    elif flag == 'off':
        window[xmin:xmax+1, ymin:ymax+1]=np.maximum(window[xmin:xmax+1, ymin:ymax+1]-1, 0)
    elif flag == 'toggle':
        window[xmin:xmax+1, ymin:ymax+1]+=2
print('part2: ', window.sum().sum())


# ### Day7

f = open('./2015/inputs/input7.txt').read().splitlines()

calc = dict()
results = dict()

for fi in f:
    (ops, res) = fi.split('->')
    calc[res.strip()] = ops.strip().split(' ')

def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass
    
    if name not in results:
        ops = calc[name]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
                res = calculate(ops[0]) & calculate(ops[-1])
            if op == 'OR':
                res = calculate(ops[0]) | calculate(ops[-1])
            if op == 'RSHIFT':
                res = calculate(ops[0]) >> calculate(ops[-1])
            if op == 'LSHIFT':
                res = calculate(ops[0]) << calculate(ops[-1])
            if op == 'NOT':
                res = ~calculate(ops[1]) & 2**16-1
        results[name] = res
    return results[name]

geta = calculate('a')
print('part1: ', geta)

calc['b'] = str(geta)
results = dict()
results['b'] = geta
print('part2: ', calculate('a'))