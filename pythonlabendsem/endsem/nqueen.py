import random

# evaluate the number of conflicts between queens
def evaluate(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i]-board[j]) == j-i:
                conflicts += 1
    return conflicts

# generate a random arrangement of queens on the board
def generate_board(n):
    return [random.randint(0,n-1) for i in range(n)]

# make a move that results in fewer conflicts
def make_move(board):
    n = len(board)
    current_conflicts = evaluate(board)
    for i in range(n):
        for j in range(n):
            if j != board[i]:
                new_board = board.copy()
                new_board[i] = j
                new_conflicts = evaluate(new_board)
                if new_conflicts < current_conflicts:
                    return new_board
    return board

# solve the 8 queens problem using Hill Climbing algorithm
def solve(n):
    board = generate_board(n)
    while True:
        new_board = make_move(board)
        if new_board == board:
            return board
        board = new_board

# print the solution
n = 8
solution = solve(n)
for i in range(n):
    for j in range(n):
        if solution[i] == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
