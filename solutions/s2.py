with open('../inputs/input2.txt') as f:
    lines = f.read().splitlines()

split_lines = [l.split(" ") for l in lines]
direction, position = map(list, zip(*split_lines))
position = [int(i) for i in position]

# part1
depth = 0
pos = 0
for d, p in zip(direction, position):
    if d == 'forward':
        pos += p
    if d == 'up':
        depth -= p
    if d == 'down':
        depth += p
print(depth*pos)

# part2
aim = 0
hori = 0
depth = 0
for d, p in zip(direction, position):
    if d == 'down':
        aim += p
    if d == 'up':
        aim -= p
    if d == 'forward':
        hori += p
        depth += aim * p
print(hori*depth)