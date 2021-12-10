with open('../inputs/input10.txt') as f:
    files = f.read().splitlines()

def day10(toy):
    pairs =['<>', '[]', '()', '{}']
    left = ['<', '[', '(', '{']
    illegal = []
    new_toy = toy.copy()    

    for t in toy:
        line = t
        while ('<>' in t) or ('[]' in t) or ('()' in t) or ('{}' in t):
            for p in pairs:
                t = t.replace(p, "")
        for s in left:
            while (s in t):
                t = t.replace(s, "")
        if len(t)>0:
            illegal.append(t[0])
            new_toy.remove(line)

    print('Part 1: ', illegal.count(')')*3 + illegal.count(']')*57 + illegal.count('}')*1197 + illegal.count('>')*25137)
    
    auto_complete = []  
    dict_pairs = {'<':'>', '{':'}', '[':']', '(':')'}
    dict_points = {')':1, ']':2, '}':3, '>':4}

    for t in new_toy:
        while ('<>' in t) or ('[]' in t) or ('()' in t) or ('{}' in t):
            for p in pairs:
                t = t.replace(p, "")
        s = t[::-1]
        auto_complete.append(''.join([dict_pairs[si] for si in s]))

    list_score = []
    for a in auto_complete:
        score = 0
        for ai in a:
            score = 5*score + dict_points[ai]
        list_score.append(score)
    list_score = sorted(list_score)

    print('Part 2: ', list_score[int(len(list_score)/2)])

day10(files)