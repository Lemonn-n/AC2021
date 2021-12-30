### Day13

f = open('./2015/inputs/input13.txt').read().splitlines()
f = [fi.replace('.', '') for fi in f]
f = [fi.split() for fi in f]

guest = set()
happy = dict()

for fi in f:
    guest.add(fi[0])
    happy.setdefault(fi[0], dict())[fi[-1]]=int(fi[3])*1 if fi[2]=='gain' else int(fi[3])*(-1)

from itertools import permutations

max_happy = 0
for item in permutations(guest):
    item = list(item)
    itemR = item[1:]+[item[0]]
    itemL = [item[-1]]+item[:-1]
    item_happy = sum([happy[item[i]][itemR[i]]+happy[item[i]][itemL[i]] for i in range(len(guest))])
    max_happy = max(max_happy, item_happy)
    
print('part1: ', max_happy)

happy['Me'] = dict()
for g in guest:
    happy[g]['Me'] = 0
    happy['Me'][g] = 0
guest.add('Me')

max_happy = 0
for item in permutations(guest):
    item = list(item)
    itemR = item[1:]+[item[0]]
    itemL = [item[-1]]+item[:-1]
    item_happy = sum([happy[item[i]][itemR[i]]+happy[item[i]][itemL[i]] for i in range(len(guest))])
    max_happy = max(max_happy, item_happy)
print('part2: ', max_happy)

### Day14

f = open('./2015/inputs/input14.txt').read().splitlines()
f = [fi.split() for fi in f]
f = [(fi[0], int(fi[3]), int(fi[6]), int(fi[-2])) for fi in f]

time = 2503

def dist(time):
    dist = []
    for fi in f:
        t1, rem1 = int(time/(fi[2]+fi[3])), time%(fi[2]+fi[3])
        dist2 = fi[1]*fi[2] if rem1 >= fi[2] else fi[1]*rem1
        dist.append(fi[1] * t1 * fi[2] + dist2)
    return dist

print('part1: ', max(dist(time)))

point = [0]*len(f)
for i in range(1, time+1):
    dist_i = dist(i)
    for i in range(len(dist_i)):
        if dist_i[i] == max(dist_i):
            point[i] += 1

print('part2:, ', max(point))

### Day15

f = open('./2015/inputs/input15.txt').read().splitlines()

item = [fi.split(':')[0] for fi in f]
f = [fi.split(':')[1].strip() for fi in f]
f = [fi.split(',') for fi in f]
f = [[fii.split() for fii in fi] for fi in f]
itemd = dict()
for i in range(len(item)):
    for j in f[i]:
        itemd.setdefault(item[i], dict())[j[0]]=int(j[1])

score = 0
           
for sp in range(0, 100):
    for pn in range(0, 100-sp):
        for fr in range(0, 100-sp-pn):
            su = 100 - sp - pn - fr
            item_amt = [sp, pn, fr, su]
            cap = max(sum([itemd[i]['capacity']*a for i,a in zip(item, item_amt)]), 0)
            dur = max(sum([itemd[i]['durability']*a for i,a in zip(item, item_amt)]), 0)
            fla = max(sum([itemd[i]['flavor']*a for i,a in zip(item, item_amt)]), 0)
            tex = max(sum([itemd[i]['texture']*a for i,a in zip(item, item_amt)]), 0)
            score = max(cap * dur * fla * tex, score)

print('part1: ', score)

score = 0
           
for sp in range(0, 100):
    for pn in range(0, 100-sp):
        for fr in range(0, 100-sp-pn):
            su = 100 - sp - pn - fr
            item_amt = [sp, pn, fr, su]
            cap = max(sum([itemd[i]['capacity']*a for i,a in zip(item, item_amt)]), 0)
            dur = max(sum([itemd[i]['durability']*a for i,a in zip(item, item_amt)]), 0)
            fla = max(sum([itemd[i]['flavor']*a for i,a in zip(item, item_amt)]), 0)
            tex = max(sum([itemd[i]['texture']*a for i,a in zip(item, item_amt)]), 0)
            cal = sum([itemd[i]['calories']*a for i,a in zip(item, item_amt)])
            if cal == 500:
                score = max(cap * dur * fla * tex, score)

print('part2: ', score)

### Day16

f = open('./2015/inputs/input16.txt').read().splitlines()
f = [fi.replace(':', '').replace(',', '').split() for fi in f]
sued = dict()
for fi in f:
    sued.setdefault(fi[1], dict())
    sued[fi[1]][fi[2]] = int(fi[3])
    sued[fi[1]][fi[4]] = int(fi[5])
    sued[fi[1]][fi[6]] = int(fi[7])

paperd = {
    'children':3,
    'cats':7,
    'samoyeds':2,
    'pomeranians':3,
    'akitas':0,
    'vizslas':0,
    'goldfish':5,
    'trees':3,
    'cars':2,
    'perfumes':1}

sue_set = set(sued.keys())
for kp,vp in paperd.items():
    new_set = set([k for k in sued.keys() if sued[k].get(kp) is None or sued[k].get(kp)==vp])
    sue_set = sue_set & new_set

print('part1: ', sue_set)

paperd2 = {
    'children':3,
    'samoyeds':2,
    'akitas':0,
    'vizslas':0,
    'cars':2,
    'perfumes':1}

sue_set = set(sued.keys())
for kp,vp in paperd2.items():
    new_set = set([k for k in sued.keys() if sued[k].get(kp) is None or sued[k].get(kp)==vp])
    sue_set = sue_set & new_set
set_cats = set([k for k in sued.keys() if sued[k].get('cats') is None or sued[k].get('cats')>7])
set_trees = set([k for k in sued.keys() if sued[k].get('trees') is None or sued[k].get('trees')>3])
set_pomeranians= set([k for k in sued.keys() if sued[k].get('pomeranians') is None or sued[k].get('pomeranians')<3])
set_goldfish = set([k for k in sued.keys() if sued[k].get('goldfish') is None or sued[k].get('goldfish')<5])
sue_set = sue_set & set_cats & set_trees & set_pomeranians & set_goldfish

print('part2: ', sue_set)

### Day17

f = list(map(int, open('./2015/inputs/input17.txt').read().splitlines()))

from itertools import combinations

cnt = []
for i in range(len(f)):
    for j in combinations(f, i):
        if sum(list(j))==150:
            cnt.append(len(j))
print('part1: ', len(cnt))
print('part2: ', cnt.count(min(cnt)))

### Day18

f = open('./2015/inputs/input18.txt').read().splitlines()
f = [fi.replace('#', '1').replace('.', '0') for fi in f]
f = ['0'+fi+'0' for fi in f]
f.insert(0, ''.join(['0']*(len(f)+2)))
f.append(''.join(['0']*(len(f)+1)))
f = [[int(fii) for fii in fi] for fi in f]

import copy

def step(n, f):
    for ni in range(n):
        newf = copy.deepcopy(f)
        for i in range(1, len(f)-1):
            for j in range(1, len(f)-1):
                neighbor = sum([f[i-1][j], f[i-1][j+1], f[i][j+1], f[i+1][j+1], f[i+1][j], f[i-1][j-1], f[i][j-1], f[i+1][j-1]])
                newf[i][j] = 1 if (f[i][j]==1 and neighbor in [2, 3]) or (f[i][j]==0 and neighbor==3) else 0
        f = newf
    return sum([fi.count(1) for fi in f])

print('part1: ', step(100, f))

def step2(n, f):
    f[1][1], f[1][len(f)-2], f[len(f)-2][1], f[len(f)-2][len(f)-2] = 1, 1, 1, 1
    for ni in range(n):
        newf = copy.deepcopy(f)
        for i in range(1, len(f)-1):
            for j in range(1, len(f)-1):
                neighbor = sum([f[i-1][j], f[i-1][j+1], f[i][j+1], f[i+1][j+1], f[i+1][j], f[i-1][j-1], f[i][j-1], f[i+1][j-1]])
                newf[i][j] = 1 if (f[i][j]==1 and neighbor in [2, 3]) or (f[i][j]==0 and neighbor==3) else 0
        f = newf
        f[1][1], f[1][len(f)-2], f[len(f)-2][1], f[len(f)-2][len(f)-2] = 1, 1, 1, 1
    return sum([fi.count(1) for fi in f])

print('part2: ', step2(100, f))      
