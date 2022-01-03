### day 19

f = open('./2015/inputs/input19.txt').read().split('\n\n')
med = f[1].split('\n')[0]

from collections import defaultdict
replaced = defaultdict(list)
for r in f[0].split('\n'):
    k,v = r.split(' => ')
    replaced[k].append(v)

def replace_nth(s, old, new, n):
    find = s.find(old)
    i = find != -1
    while find != -1 and i != n:
        find = s.find(old, find + 1)
        i += 1
    if i == n:
        return s[:find] + new + s[find+len(old):]
    return s

def grow(med):
    final_new_med = []
    for m in med:
        new_med = []
        for r in replaced.keys():
            n = m.count(r)
            for ni in range(n):
                for v in replaced[r]:
                    new_med.append(replace_nth(m, r, v, ni+1))
        new_med = list(set(new_med))
        final_new_med += new_med
    return final_new_med

print('part1: ', len(grow([med])))

import re

# process everything backward (right to left)
input1 = open('./2015/inputs/input19.txt').read()
molecule = input1.split('\n')[-2][::-1]
reps = {m[1][::-1]: m[0][::-1] 
        for m in re.findall(r'(\w+) => (\w+)', input1)}

count = 0
while molecule != 'e':
    molecule = re.sub('|'.join(reps.keys()), lambda x: reps[x.group()], molecule, 1)
    count += 1

print('part2: ', count)

### day 20

f = 34000000
try1 = 900000

import numpy as np

house = np.zeros(try1)
house2 = np.zeros(try1)
for i in range(1, try1):
    house[i::i] += 10*i
    house2[i::i][:50] += 11* i
print('part1: ', np.nonzero(house>=f)[0][0])
print('part2: ', np.nonzero(house2>=f)[0][0])   

### day 21

boss = (100, 8, 2)
weapon = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armor = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5), (0, 0, 0)]
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3), (0, 0, 0)]

def fight(boss, player):
    p_h, b_h = player[0], boss[0]
    while min(p_h, b_h)>0:
        b_h -= max(player[1] - boss[2], 1)
        if b_h <= 0:
            return True
        p_h -= max(boss[1] - player[2], 1)
        if p_h <= 0:
            return False

from itertools import combinations

m = 1000
for w in weapon:
    for a in armor:
        for r1, r2 in combinations(rings, 2):
            cost = w[0]+a[0]+r1[0]+r2[0]
            dmg = w[1]+a[1]+r1[1]+r2[1]
            arm = w[2]+a[2]+r1[2]+r2[2]
            if fight(boss, (100, dmg, arm)):
                m = min(m, cost)
print('part1: ', m)

m = 0
for w in weapon:
    for a in armor:
        for r1, r2 in combinations(rings, 2):
            cost = w[0]+a[0]+r1[0]+r2[0]
            dmg = w[1]+a[1]+r1[1]+r2[1]
            arm = w[2]+a[2]+r1[2]+r2[2]
            if not fight(boss, (100, dmg, arm)):
                m = max(m, cost)
print('part2: ', m)

### day 22

def sim(actions, part):
    boss_hp, boss_dmg = 51, 9
    hp, mana, armor = 50, 500, 0
    turn, turn_c = 0, 0
    mana_spent = 0
    poison_left, shield_left, recharge_left = 0, 0, 0
    my_turn = 1
    spell_cost = {'M':53, 'D':73, 'S':113, 'P':173, 'R':229}
    
    while True:
        if len(actions)-1 < turn_c:
            return 0
        if poison_left:
            poison_left = max(poison_left-1, 0)
            boss_hp -= 3
        if shield_left:
            shield_left = max(shield_left-1, 0)
            armor = 7
        else:
            armor = 0
        if recharge_left:
            recharge_left = max(recharge_left-1, 0)
            mana += 101
        if my_turn == 1:
            if part == 2:
                hp -= 1
                if hp <= 0:
                    return 0
            action = actions[turn_c]
            mana -= spell_cost[action]
            mana_spent += spell_cost[action]
            if action == 'M':
                boss_hp -= 4
            elif action == 'D':
                boss_hp -= 2
                hp += 2
            elif action == 'P':
                if poison_left:
                    return 0
                poison_left = 6
            elif action == 'S':
                if shield_left:
                    return 0
                shield_left = 6
            elif action == 'R':
                if recharge_left:
                    return 0
                recharge_left = 5
            if mana < 0:
                return 0
        if boss_hp <= 0:
            return mana_spent
        if my_turn == -1:
            hp -= max(boss_dmg-armor, 1)
            if hp <= 0:
                return 0
        if my_turn == 1:
            turn_c += 1
        my_turn = -my_turn
        turn += 1

def iter_actions(pos):
    actions[pos] = 'DSPRM'['MDSPR'.index(actions[pos])]
    if actions[pos] == 'M':
        if pos+1 <= len(actions):
            iter_actions(pos+1)

for part in (1, 2):
    actions = ['M']*20
    min_spent = 10**6
    for i in range(10**6):
        result = sim(actions, part)
        if result:
            min_spent = min(result, min_spent)
        iter_actions(0) 
    print('part'+str(part)+': ', min_spent)