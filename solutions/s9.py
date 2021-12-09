with open('../inputs/input9.txt')as f:
    files = f.read().splitlines()
files = [[int(i) for i in t] for t in files]
    
def local_min(toy):    
    local_min = []
    local_min_cor = []
    max_row = len(toy)
    max_col = len(toy[0])

    for i in range(max_row):
        for j in range(max_col):
            right = toy[i][min(j+1, max_col-1)]
            left = toy[i][max(j-1, 0)]
            up = toy[max(0, i-1)][j]
            down = toy[min(max_row-1, i+1)][j]
            if j+1 == max_col:
                right = 10
            if j-1 < 0:
                left = 10
            if i-1 < 0:
                up = 10
            if i+1 == max_row:
                down = 10
            
            if toy[i][j] < min(right, left, up, down):
                local_min.append(toy[i][j])
                local_min_cor.append([i, j])
                
    return sum(local_min)+len(local_min), local_min_cor

def local_basin(toy, cor):    
    new_basin = [(cor[0], cor[1])]
    final_basin = [(cor[0], cor[1])]
    max_row = len(toy)
    max_col = len(toy[0])
    
    while len(new_basin)>0:
        add_basin = []
        for i in range(len(new_basin)):
            x, y = new_basin[i][0], new_basin[i][1]
            # right path
            for j in range(y+1, max_col):
                if ((toy[x][j] == 9) or (toy[x][y] >= toy[x][j])):
                    break
                else:
                    add_basin.append((x, j))
            # left path
            for j in range(y-1, -1, -1):
                if ((toy[x][j] == 9) or (toy[x][y] >= toy[x][j])):
                    break
                else:
                    add_basin.append((x, j))
            # up path
            for i in range(x-1, -1, -1):
                if ((toy[i][y] == 9) or (toy[x][y] >= toy[i][y])):
                    break
                else:
                    add_basin.append((i, y))
            # down path
            for i in range(x+1, max_row):
                if ((toy[i][y] == 9) or (toy[x][y] >= toy[i][y])):
                    break
                else:
                    add_basin.append((i, y))
        add_basin = list(set(add_basin) - set(new_basin))
        final_basin = list(set(final_basin + add_basin))
        new_basin = add_basin
 
    return len(final_basin)
            
sum_min, local_min_cor = local_min(files)
print('Part 1: ', sum_min)

local_basin_area = []
for mcor in local_min_cor:
    local_basin_area.append(local_basin(files, mcor))

local_basin_area = sorted(local_basin_area, reverse=True)[:3]
print('Part 2: ', local_basin_area[0] * local_basin_area[1] * local_basin_area[2])