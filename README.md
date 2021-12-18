# AC2021
Advent of Code 2021

### Items learned  
d1: numpy.roll to get lag

d2: split lines using string.split()

d3: using int() for binary conversion

d4: 
- my solution: for all numbers run each board until win and record steps take, take min step and max step for part 1 and part 2; using flags to track each position and mark to determine win condition
- online solution: for all boards, start with 1st number and check if any win for part 1; for part 2, start with all numbers and pop 1 each time and check if all win, stop until all but 1 win as last win; using set operation to determine win condition
- my struggles (data loading): I split original input file into 2, still get the logics/index of data structure wrong without realizing it
- online better: using f.read.split('\n\n') to load to different objects; using zip(*list) to transpose list; using itertools.chain to combine lists; 

d5:
- my solution: derive each horizontal, vertical, and diagonal lines separately and convert to sets, then use set.symmetric_difference_update(^=) to find elements only exist once
- online solution: using same logic for all 3 types of lines, then use collections.Counter to count each point
- my struggles (logic loophole): in set operation logic, every time only compare 2 and drop common ones then move to next, if the common point shows up on 3rd time, it will be considered as non-common one as it was dropped out in current tracking/comparing set, have to use another list to track all the common ones dropped
- online better: using re to load data easier with simplier structure; using Counter to track each point instead of comprison; using common logics for all lines

d6:
- my solution: go through days, each day go through fish
- online solution: go through days, count fishes of each day cycle type
- my stuggles (effiency): it looks freezing after 100+ days, n (days) * n (fish exponential grow)
- online better: only O(n) - linear to days

d11:
- original logics loophole: just loop each row, then each column, find >9 to radiate, however, this will not cover the squid radiate in the bottom, then backradiate to the top of matrix, and trigger new rounds of radition on the top, hence it will not work, it will break on step 2 of the large toy sample

d13:
- np.array reverse in different axis, np.nditer for interation and modification

d12:
- collection.defaultdict to setup dict without initianizing/key error
- I worked on the logics for a while, even with the online solution, still couldn't fully understand the logics of path/recursion, especially for part 2, with print help on the toy sample, the part 2 direct end path is actually part 1 direct end path, the added new path actually all calling from part 1 in the code - I couldn't wrap my head around it, may come back to visit it later

d15:
- originally I wrote a dijkstra following wiki's algorithm description, it worked for toy case, but run out of max recusion limit for input :(
- then I came up nwith a constant time seaching method for down/right directional search, it also works for toycase, but a littl off for real input - find a online solution and spent a whole day testing the input data trying to find edge case where my solution will break and back trace the path - it can not solve when path has a 9 surronding by small number cases - optimal path will have a 'loop' - going down, then up then down, instead of always going right and down
- at least learned these things: index with '//' and '%'  in list instead of using np 2D array, np.diagonal(), np.indices(), np.vstack, np.hstack
