# my solution

with open('../inputs/input4-number.txt') as f:
    number = f.read().splitlines()
number = [n.split(",") for n in number][0]

with open('../inputs/input4-board.txt') as f:
    board = f.read().splitlines()

board1 = [] # prepare each board

n = int((len(board)+1)/6) # number of boards

for i in range(n):
    bi = board[i*6]
    for j in range(i*6+1, i*6+6):
        if j < len(board):
            bi = bi + " " + board[j]
    board1.append(bi)

board1 = [b1.split(" ") for b1 in board1]
# remove empty string
for i, b1 in enumerate(board1):
    board1[i] = [bi for bi in b1 if len(bi)>0]

# run the game

def check_ni_boardi(list_l, number_i, mark):
    if number_i in list_l:
        mark[list_l.index(number_i)] = 1
    return mark

def update_flag(mark):
    flag = [0]*10
    for i in range(5):
        flag[i] = sum(mark[i*5:(i+1)*5]) # horizontal
    for i in range(5, 10):
        flag[i] = sum([mark[ind] for ind in range(i-5, 25, 5)]) # vertical
    return flag 

def run1_board(boardi, number):
    mark = [0]*25
    seq = 0
    for ni in number:
        mark = check_ni_boardi(boardi, ni, mark)
        flag = update_flag(mark)
        if max(flag) == 5:
            break
        seq = seq + 1
    unmarked = [int(j) for i,j in zip(mark, boardi) if i==0]
    score = int(ni) * sum(unmarked) 
    return seq, score

out = []
for b1 in board1:
    out.append(run1_board(b1, number))

# part 1 - get first winning score

rounds, scores= zip(*out)
print(scores[rounds.index(min(rounds))])

# part 2 - get last winning score

rounds, scores= zip(*out)
print(scores[rounds.index(max(rounds))])


# Online solution I found
# -- much more effient in loading data and do logics

with open('../inputs/input4.txt') as f:
    numbers, *boards = f.read().split('\n\n')
    numbers = list(map(int, numbers.split(',')))
    boards = [[[int(n) for n in row.split()] for row in board.splitlines()] for board in boards]

from itertools import chain

def find_win_score():
    called = []
    for num in numbers:
        called.append(num)
        for board in boards:
            if any(set(line) < set(called) for line in chain(board, zip(*board))):
                unmarked = {n for row in board for n in row} - set(called)
                return sum(unmarked) * num

def find_losing_score():
    called = numbers.copy()
    while called:
        last = called.pop()
        for board in boards:
            if not any(set(line) < set(called) for line in chain(board, zip(*board))):
                unmarked = {n for row in board for n in row} - {last, *called}
                return sum(unmarked) * last
print(find_win_score())
print(find_losing_score())