### day4
* use hash to to md5 hash
* using itertools.count() to loop to infinity - somehow much faster than counting
* use threading to do multi-threading 

### day7
* when using &, |, ~ operator on int, it does bitwise operation instead of logic operation (assuming any positive int is True)
* originally my thought: based on instruction length, find initial wire to start, then find instruction with only known wires, so on and so forth, basically need to sort instructions in executable order; the online solution I found using dict instead of sort instructions and recursive solve the needed wire

### day8
* use eval to evaluate string input

### day9
* set defulat dict of dict: "dict1.setdefault(key1, dict())[key2]=int(value2)"
* use itertools.permutations to get all permutation
* use map and lambda to process adjacent elements in lists

### day10
* use itertools.groupby to count consecutive chars in string

### day11
* re: find >=2 repeated lowercase: '[a-z]\1'
* re: find groups of pattern: '([a-z])(z*)$' - group(0) will be input string, group(1) all exclude ending 'z's, group(2) all ending 'z's
* ord() convert letter to number, chr() convert number to letter

### day12
* json package, map functions

### day19
* I figure out part 1, however, it will take forever to run part 2 (way too inefficient after step 8), found online one for part 2

### day20
* about 'infinite large', day4 ways of counting and threading doesnot work, use np to work efficiently on large number, np.nonzero() as mask

### day22
* iteraiton through sequence of chars:
```a = ['a']*5
def iter_a(pos):
    a[pos]='bcdea'['abcde'.index(a[pos])]
    if a[pos]=='a':
        iter_a(pos+1)
for i in range(20):
    print(a)
    iter_a(0)```