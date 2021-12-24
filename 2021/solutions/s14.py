with open('../inputs/input14.txt') as f:
    files = f.read().split('\n\n')

s0 = files[0]

import re
dict_instruct = {}
instruct = re.findall('(\w+) -> (\w+)\n', files[1])
for x,y in instruct:
    dict_instruct[x] = y

from collections import defaultdict

def polymer(s0, dict_instruct, step=1):

    count_instruct = defaultdict(int)

    for i in range(len(s0)-1):
        count_instruct[s0[i:i+2]]+=1
        
    for i in range(step):
        new_count_instruct = count_instruct.copy()
        for j in count_instruct.keys():
            freq = count_instruct[j]
            if freq > 0:
                new_count_instruct[j[0]+dict_instruct[j]] += freq
                new_count_instruct[dict_instruct[j]+j[1]] += freq
                new_count_instruct[j] -= freq
  
        count_instruct = new_count_instruct
    
    dict_cnt = defaultdict(int)
    for k,v in count_instruct.items():
        if v>0:
            dict_cnt[k[0]]+=v
            dict_cnt[k[1]]+=v
    dict_cnt[s0[0]]+=1  # 1st and last char counted only once, all the rest counted twice
    dict_cnt[s0[-1]]+=1
    return max(dict_cnt.values())/2 - min(dict_cnt.values())/2

print('part 1: ', polymer(s0, dict_instruct, step=10))
print('part 2: ', polymer(s0, dict_instruct, step=40))

# original looping solution that will freeze at large steps
def polymer(s0, dict_instruct, step=1):
    new_s = s0
    for i in range(step): 
        out_s = ''
        for s in range(len(new_s)-1):
            out_s += new_s[s]+dict_instruct[new_s[s:s+2]]
        out_s += new_s[-1]
        new_s = out_s
    out_count = []
    for i in set(out_s):
        # out_count.append((i, out_s.count(i)))
        out_count.append(out_s.count(i))
    out_count = sorted(out_count)
    return out_count[-1]-out_count[0]           
print('part 1: ', polymer(s0, dict_instruct, step=10))