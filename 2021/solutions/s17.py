f = open('../inputs/input17.txt').read().splitlines()
x_range = [int(x) for x in f[0].split(',')[0].split('=')[1].split('..')]
y_range = [int(y) for y in f[0].split(',')[1].split('=')[1].split('..')]
print(x_range, y_range)

def inRange(pos, rangex, rangey):
    return (pos[0] in range(rangex[0], rangex[1]+1)) and (pos[1] in range(rangey[0], rangey[1]+1))

def step(x0, y0, rangex, rangey):
    pos = [(x0, y0)]
    vx, vy = x0, y0
    while True:
        if inRange(pos[-1], rangex, rangey):
            return (x0, y0)
        if pos[-1][1]<rangey[0]:
            return -1
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        pos.append((pos[-1][0]+vx, pos[-1][1]+vy))

# part1:
# at vy>0 velocity, it will reach y-pos=0 with velocity vy-1
# if vy<0, it will miss the target is vy < y-target min
# so, y-target min = -vy - 1 --> vy = -y-taget min -1
# max height= vy * (vy+1)/2

vy = -y_range[0]-1
print('part 1: ', vy * (vy+1)/2)

init = []
for xi in range(1, x_range[1]+1):
    for yi in range(y_range[0], -y_range[0]):
        if step(xi, yi, x_range, y_range) != -1:
            init.append(step(xi, yi, x_range, y_range))
print('part 2: ', len(init))