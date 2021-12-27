### Day 8

f = open('./2015/inputs/input8.txt').read().splitlines()

print('part1: ', sum([len(si)-len(eval(si)) for si in f]))
print('part2: ', sum([si.count('"') + si.count('\\') + 2 for si in f]))

### Day 9

f = open('./2015/inputs/input9.txt').read().splitlines()

places = set()
distances = dict()

for fi in f:
    (source, _, dest, _, dist) = fi.split()
    places.add(source)
    places.add(dest)
    distances.setdefault(source, dict())[dest]=int(dist)
    distances.setdefault(dest, dict())[source]=int(dist)

import sys
from itertools import permutations

shortest = sys.maxsize
longest = 0

for item in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], item[:-1], item[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print("part1: %d" % (shortest))
print("part2: %d" % (longest))

### Day 10

f = '1321131112'

from itertools import groupby

def repeat(f, n):
    for i in range(n):
        f = ''.join([(str(sum(1 for _ in group))+_) for _, group in groupby(f)])
    return f
print('part1: ', len(repeat(f, 40)))
print('part2: ', len(repeat(f, 50)))

### Day 11

f = 'vzbxkghb'

import re

def nextpwd(f):
    while True:
        f = re.sub(r'([a-y])(z*)$', lambda x: chr(ord(x.group(1))+1) + len(x.group(2))*"a", f)
        if ('i' in f or 'o' in f or 'l' in f) or \
        (len(re.findall(r'([a-z])\1', f))<2) or \
        (len([1 for x,y,z in zip(f, f[1:], f[2:]) if ord(z)-ord(y)==1 and ord(y)-ord(x)==1])==0):
            continue
        return f
        
print('part1: ', nextpwd(f))
print('part2: ', nextpwd(nextpwd(f)))  

### Day 12

import json
f = open('./2015/inputs/input12.txt').read().splitlines()[0]
f = json.loads(f)

def sum1(obj):
    if type(obj) is int:
        return obj  
    if type(obj) is list:
        return sum(map(sum1, obj))    
    if type(obj) is dict:
        vals = obj.values()
        return sum(map(sum1, vals))    
    else:
        return 0

def sum2(obj):
    if type(obj) is int:
        return obj   
    if type(obj) is list:
        return sum(map(sum2, obj))    
    if type(obj) is dict:
        vals = obj.values()
        if 'red' in vals:
             return 0
        return sum(map(sum2, vals))    
    else:
        return 0
print('part 1: ', sum1(f))
print('part 2: ', sum2(f))