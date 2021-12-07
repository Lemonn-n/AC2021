with open('../inputs/input7.txt')as f:
    files = f.read().split(",")
files = [int(f) for f in files]

import statistics
import numpy as np

# part 1
median = statistics.median(files)
print('part 1: ', int(sum(abs(np.array(files)-median))))

# part 2
fuel = []
for i in range(min(files), max(files)):
    step = abs(np.array(files)-i)
    fuel.append(sum(step * (1+step)/2))
print('part 2: ', int(min(fuel)))