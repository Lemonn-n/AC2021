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

