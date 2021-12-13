with open('../inputs/input13.txt') as f:
    files = f.read().split('\n\n')
coord = [c.split(',') for c in files[0].split('\n')]
coord = [[int(c) for c in cor] for cor in coord]

import re
instruction = re.findall('(\w+)=(\w+)', files[1])

x, y = zip(*coord)

import numpy as np
paper = np.zeros((max(y)+1, max(x)+1))

for c in coord:
    paper[c[1], c[0]] = 1

for step,i in enumerate(instruction):
    fold_line = int(i[1])
    if i[0]=='y':        
        paper[fold_line, :] = 0
        paper_up = paper[0:fold_line, :]
        paper_down = paper[fold_line+1:, :]
        paper_down = paper_down[::-1, :]
        paper = paper_up+paper_down
        print(step+1, i , (paper>0).sum())

    else:
        paper[:, fold_line] = 0
        paper_left = paper[:, 0:fold_line]
        paper_right = paper[:, fold_line+1:]
        paper_right = paper_right[:,::-1]
        paper = paper_left+paper_right
        print(step+1, i, (paper>0).sum())

# Part2 help visualizing
print((paper>0).astype(int))