with open('../inputs/input12.txt') as f:
    files = f.read().splitlines()

# ------------------------------
# create connect point dictionary
# ------------------------------
import re

pairs = []
for t in files:
    pairs += list(re.findall('(\w+)-(\w+)', t))

unique_point = list(set(list(zip(*pairs))[1]) | set(list(zip(*pairs))[0]))

dict_connect = {}
for p in unique_point:
    p_pair = [list(pair) for pair in pairs if p in pair]
    next_point = []
    for s in p_pair:
        next_point += s
    dict_connect[p] = list(set(next_point) - {p} - {'start'})
del dict_connect['end']
print(dict_connect)

# ------------------------------
# create connect point dictionary - alternative online solution
# ------------------------------
# using defaultdict can aovid key error, no need to initiaize a value first
from collections import defaultdict

dict_connect = defaultdict(list)
for f in files:
    pair = f.strip().split('-')
    for p1, p2 in zip(pair, reversed(pair)):
        if p2 != 'start':
            dict_connect[p1].append(p2)
del dict_connect['end']
print(dict_connect)

def count(dict_connect, path=['start']):
    count_path = 0
    for node in dict_connect[path[-1]]:
        if node.isupper() or not node in path:
            if node == 'end':
                count_path += 1
                # print('part1: end: ', path, node)
            else:
                count_path += count(dict_connect, path+[node])
    return count_path
        
print('part 1: ', count(dict_connect))

def count2(dict_connect, path=['start']):
    count_path = 0
    for node in dict_connect[path[-1]]:
        if node == 'end':
            count_path += 1
            # print('part2: end: ', path, node)
        else:
            if node.islower() and node in path:
                count_path += count(dict_connect, path+[node])
            else:
                count_path += count2(dict_connect, path+[node])
    return count_path
     
print('part 2: ', count2(dict_connect))