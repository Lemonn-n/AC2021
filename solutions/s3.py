with open('../inputs/input3.txt') as f:
    lines = f.read().splitlines()

ll = []
for l in lines:
    ll.append([li for li in l])

# part1

from statistics import mode

gamma = []
for i in range(len(ll[0])):
    xi = []
    for lli in ll:
        xi.append(lli[i])        
    gamma.append(mode(xi))
gamma = [int(i) for i in gamma]
epsilon = [1-i for i in gamma]
gamma = int(''.join([str(i) for i in gamma]), 2)
epsilon = int(''.join([str(i) for i in epsilon]), 2)
print(gamma, epsilon, gamma*epsilon)

# part2
def findO2(l):
    
    def getListByOne(l, i):
        xi = []
        for lli in l:
            xi.append(lli[i])
        if xi.count('1') >= xi.count('0'):
            pos = [i for i, x in enumerate(xi) if x == "1"]
        else:
            pos = [i for i, x in enumerate(xi) if x == "0"]

        out = []
        for p in pos:
            out.append(l[p])
        return out, len(out)

    subl = l
    lenl = len(l)
    i = 0
    while lenl > 1:
        subl, lenl = getListByOne(subl, i)
        i += 1
    
    if lenl==1:
        O2 = int(''.join([str(i) for i in subl[0]]), 2)
    return O2


def findCO2(l):
    
    def getListByOne(l, i):
        xi = []
        for lli in l:
            xi.append(lli[i])
        if xi.count('0') <= xi.count('1'):
            pos = [i for i, x in enumerate(xi) if x == "0"]
        else:
            pos = [i for i, x in enumerate(xi) if x == "1"]

        out = []
        for p in pos:
            out.append(l[p])
        return out, len(out)

    subl = l
    lenl = len(l)
    i = 0
    while lenl > 1:
        subl, lenl = getListByOne(subl, i)
        i += 1
    
    if lenl==1:
        CO2 = int(''.join([str(i) for i in subl[0]]), 2)
    return CO2

O2 = findO2(ll)
CO2 = findCO2(ll)
print(O2, CO2, O2*CO2)        
    