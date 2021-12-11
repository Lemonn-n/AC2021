with open('../inputs/input11.txt') as f:
    files = f.read().splitlines()

import numpy as np    
files = np.array([[int(f) for f in file] for file in files])

def radiate(minitoy, i, j):
    for ii in range(max(0, i-1), min(minitoy.shape[0], i+2)):
        for jj in range(max(0, j-1), min(minitoy.shape[1], j+2)):
            minitoy[ii][jj] += 1
    minitoy[i][j] -= 1
    return minitoy

def simulation(minitoy, steps=1):
    max_row, max_col = minitoy.shape
    flash_cnt = 0
    flash_seq = []
    for step in range(steps):
        minitoy = minitoy + 1
        rad_cells = [] # cell radiated already
        new_rad = []        
        while True:
            # print(minitoy)
            for i in range(max_row):
                for j in range(max_col):
                    if minitoy[i][j] > 9:
                        new_rad.append((i, j))
            new_rad = list(set(new_rad) - set(rad_cells))
            # print("new_rad: ", new_rad)
            
            if len(new_rad) == 0:
                break

            for r in new_rad:
                minitoy = radiate(minitoy, r[0], r[1])
            rad_cells = list(set(rad_cells + new_rad))
            new_rad = []
            # print("rad_cells: ", rad_cells)
        
        for cell in rad_cells:
            minitoy[cell[0]][cell[1]] = 0
        flash_cnt += len(rad_cells)
        flash_seq.append(len(rad_cells))

    return minitoy, flash_cnt, flash_seq

print('Part 1: ', simulation(files, steps=100)[1])

s = 100 # random initial number
a, b, c = simulation(files, steps=s)
while max(c) < 100:
    s += 100
    a, b, c = simulation(files, steps=s)
print('Part 2: ', c.index(100)+1)