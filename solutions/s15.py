filename = 'input15'
# filename = 'toy15'

# works for toy case not actual input :(

import numpy as np

with open('../inputs/'+filename+'.txt') as f:
    files = f.read().splitlines()
files = np.array([[int(s) for s in file] for file in files])

list_dist = []
list_index = []
for i in range(len(files), -len(files), -1):
    list_dist.append(files[:,::-1].diagonal(i).tolist())
    list_index.append(list(zip(np.indices(files.shape)[0][:, ::-1].diagonal(i),\
    np.indices(files.shape)[1][:, ::-1].diagonal(i))))
list_dist.pop(0)
list_index.pop(0)

dict_dist = {}
for i,j in zip(list_index, list_dist):
    for ii, jj in zip(i,j):
        dict_dist[ii] = jj
dict_dist[(0,0)] = 0
        
def update_node(node, dict_dist):
    i, j = node
    up = (max(i-1, 0), j)
    left = (i, max(j-1, 0))
    if up == node:
        dict_dist[node]+=dict_dist[left]
        return dict_dist
    if left == node:
        dict_dist[node]+=dict_dist[up]
        return dict_dist
    dict_dist[node] += min(dict_dist[up], dict_dist[left])
    return dict_dist

for i in range(len(files)*2-1):
    for node in list_index[i]:
        dict_dist = update_node(node, dict_dist)
        # print(node, dict_dist[node])
print(dict_dist[(files.shape[0]-1, files.shape[1]-1)])   
               