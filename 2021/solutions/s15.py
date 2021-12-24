filename = 'input15'

# works for toy case not actual input :(

# After checking with different sizes and slices, the solution doesn't work
# because it only counts path from left or up, naively it should work for end
# point on borrom right, however, when there is 9 surrounded by small number
# on the path, it will go around and form a loopish path, such as going from
# bottom then right, then this solution no longer work, will always off by little

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
# print(dict_dist[(files.shape[0]-1, files.shape[1]-1)])   

# Online solution

def step(ij,v,p,u,w,N,I):
    # mark_from_ij
    v[ij]=True
    u.remove(ij)
    i,j=ij//N,ij%N
    for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
        if 0<=ni<N and 0<=nj<N:
            nij=N*ni+nj
            if v[nij]: continue
            if p[nij]>p[ij]+w[nij]:
                p[nij]=p[ij]+w[nij]
                u.append(nij)
    # min_unvisited
    mij=mp=I
    for uij in u:
        if p[uij]<mp:
            mij=uij; mp=p[uij]
    return mij

def solve(d):
    N=len(d); NN=N*N; I=999999 # infinity :)
    w=[] # weights, 1-dimension copy of input
    for i in range(N): w+=d[i]
    v=[False for j in range(NN)] # visited
    p=[I for j in range(NN)] # paths
    u=[] # unvisited items (ij indexes)
    p[0]=0 # start with top left corner
    u.append(0)
    uij = step(0,v,p,u,w,N,I)
    while uij!=I:
        uij = step(uij,v,p,u,w,N,I)
    return p[NN-1] # right bottom

print('Part 1: ', solve(files.tolist()))

def scale(files, j):
    file2 = files
    for i in range(1, 5, 1):
        fi = (files + i)%9
        fi = np.where(fi==0, 9, fi)
        file2 = np.hstack((file2, fi)) # horizontal

    file3 = file2
    for i in range(1, 5, 1):
        fi = (file2 + i)%9
        fi = np.where(fi==0, 9, fi)
        file3 = np.vstack((file3, fi)) # vertical
    return file3
files_large = scale(files, 5)
print('Part 2: ', solve(files_large.tolist()))