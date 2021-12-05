# my solution

with open('../inputs/input5.txt') as f:
    files = f.read().splitlines()

files = [f.split(" ->") for f in files]
files = [[f.strip().split(",") for f in file] for file in files]
files = [[[int(f) for f in ff] for ff in file] for file in files]

point1, point2 = zip(*files)

line_h = []
line_v = []
line_d = []
for p1, p2 in zip(point1, point2):
    if p1[0] == p2[0]:
        line_h.append([p1, p2]) # horziontal line
    if p1[1] == p2[1]:
        line_v.append([p1, p2]) # vertical line
    if abs(p1[0]-p2[0]) == abs(p1[1]-p2[1]):
        line_d.append([p1, p2]) # diagonal line

# generating diagonal line points
point_d = []
for i in range(len(line_d)):
    x1, y1, x2, y2 = line_d[i][0][0], line_d[i][0][1], line_d[i][1][0], line_d[i][1][1]
    xy_points = []
    for i in range(abs(x2-x1)+1):
        x_step = (x2-x1)/abs(x2-x1)
        y_step = (y2-y1)/abs(y2-y1)
        xy_points.append((x1+i*x_step, y1+i*y_step))
    point_d.append(xy_points)
point_d = tuple(point_d)

# generating horizontal line points
point_h = []
for i in range(len(line_h)):
    y1, y2 = line_h[i][0][1], line_h[i][1][1]
    y_points = list(range(min(y1, y2), max(y1, y2)+1))
    xy_points = []
    for j in y_points:
        xy_points.append((line_h[i][0][0], j))
    point_h.append(xy_points)
point_h = tuple(point_h)

# generating vertical line points
point_v = []
for i in range(len(line_v)):
    x1, x2 = line_v[i][0][0], line_v[i][1][0]
    x_points = list(range(min(x1, x2), max(x1, x2)+1))
    xy_points = []
    for j in x_points:
        xy_points.append((j, line_v[i][0][1]))
    point_v.append(xy_points)
point_v = tuple(point_v)

# part 1

point_all = point_h+point_v
point_unique = []
for p in point_all:
    point_unique += p
point_unique = set(point_unique)

# find points only in 1 line
common = []
single_set = set(point_all[0])
for p in point_all[1:]:
    pset = set(p) - set(common)    
    ci = single_set & pset
    if len(ci) > 0:
        common += list(ci)
    single_set ^= pset # keep only exist in either one

print('part1: ', len(point_unique)-len(single_set))

# part 2

point_all = point_h+point_v+point_d
point_unique = []
for p in point_all:
    point_unique += p
point_unique = set(point_unique)

# find points only in 1 line
common = []
single_set = set(point_all[0])
for p in point_all[1:]:
    pset = set(p) - set(common)    
    ci = single_set & pset
    if len(ci) > 0:
        common += list(ci)
    single_set ^= pset # keep only exist in either one

print('part2: ', len(point_unique)-len(single_set))

# =============================

# online solution

with open('../inputs/input5.txt') as f:
    data = f.read()

import re
from collections import Counter

def solution(data, part=1):
    lines = re.findall('(\d+),(\d+) -> (\d+),(\d+)', data)
    points = Counter()
    for line in lines:
        x1, y1, x2, y2 = map(int, line)
        if part == 1 and x1 != x2 and y1 != y2:  # diagonal line
            continue
        dx, dy = x2 - x1, y2 - y1
        length = max(abs(dx), abs(dy))
        x_step, y_step = dx//length, dy//length
        points.update((x1 + i*x_step, y1 + i*y_step) for i in range(length+1))
    return sum(count > 1 for count in points.values())

print('Part 1:', solution(data, part=1))
print('Part 2:', solution(data, part=2))