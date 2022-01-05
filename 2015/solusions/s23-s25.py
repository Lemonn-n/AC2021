### day23

f = list(open('./2015/inputs/input23.txt').read().splitlines())

def step(i, fi, a, b):
    ins = fi.replace(',', '').split()
    o, r = ins[0], eval(ins[1])
    if o == 'inc':
        r += 1
        i += 1
    elif o == 'hlf':
        r = r/2
        i += 1
    elif o == 'tpl':
        r = 3*r
        i += 1
    elif o == 'jmp':
        i += int(ins[-1])
    elif o == 'jie':
        i += int(ins[-1]) if r%2==0 else 1
    elif o == 'jio':
        i += int(ins[-1]) if r==1 else 1
    if ins[1] == 'a':
        a = r
    if ins[1] == 'b':
        b = r
    return (i, a, b)

i, a, b = 0, 0, 0
while i < len(f):
    fi = f[i]
    i, a, b = step(i, fi, a, b)

print('part1: ', b)

i, a, b = 0, 1, 0
while i < len(f):
    fi = f[i]
    i, a, b = step(i, fi, a, b)
    
print('part2: ', b)        

### day24

f = list(map(int, open('./2015/inputs/input24.txt').read().splitlines()))
f = sorted(f, reverse=True)

from itertools import combinations
from functools import reduce

def day24(n):
    weight = sum(f)/n
    
    for i in range(1, len(f)):
        if sum(f[:i]) >= weight:
            guess = i
            break
    p = []
    for i in range(guess-1, int(len(f)/n)):
        for j in combinations(f, i):
            if sum(j) == weight:
                p.append(j)
    min_item = min((len(pi) for pi in p))
    min_p = [reduce(lambda x, y: x*y, pi) for pi in p if len(pi)==min_item]
    return min(min_p)

print('part1: ', day24(3))
print('part2: ', day24(4)) 

### day25

row, col = 2947, 3029

def countij(i,j):
    n = 1
    for ii in range(1, i+1):
        n+=ii-1
    for ji in range(1, j+1):
        n+=(ji-1+i-1)        
    return n

def step(seq):
    num = 20151125
    for i in range(seq):
        num = (num * 252533)%33554393
    return num

print('part1: ', step(countij(col, row)-1))
print('no part 2, got my first 50* :)')