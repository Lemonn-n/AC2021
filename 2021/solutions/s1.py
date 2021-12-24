with open('../inputs/input1.txt') as f:
    lines = f.read().splitlines()

lines = [int(l) for l in lines]

import numpy as np

#par1
line_array = np.array(lines)
print('part1: ', sum((np.roll(line_array, -1)[:-1]-line_array[:-1])>0))

#part2
line_sum = line_array[:-2] + np.roll(line_array, -1)[:-2] + np.roll(line_array, -2)[:-2] 
print('part2: ', sum((np.roll(line_sum, -1)[:-1]-line_sum[:-1])>0))