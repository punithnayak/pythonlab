class Board:
    def __init__(self, state=None):
        if state is None:
            self.state = []
        else:
            self.state = state
    
    def add_queen(self, row):
        self.state.append(row)
    
    def remove_queen(self):
        self.state.pop()
    
    def is_valid(self):
        # check for conflicts
        for i in range(len(self.state)):
            for j in range(i + 1, len(self.state)):
                if self.state[i] == self.state[j] or \
                   abs(self.state[i] - self.state[j]) == j - i:
                    return False
        return True
    
    def is_goal(self):
        return len(self.state) == 8
    
    def __str__(self):
        rows = []
        for col in self.state:
            row = ['_'] * 8
            row[col] = 'Q'
            rows.append(''.join(row))
        return '\n'.join(rows)


def bfs():
    queue = [Board()]
    visited = set()
    while queue:
        board = queue.pop(0)
        if board.is_goal():
            print('solution:', tuple(board.state))
        for row in range(8):
            board.add_queen(row)
            if board.is_valid() and tuple(board.state) not in visited:
                visited.add(tuple(board.state))
                queue.append(Board(list(board.state)))
            board.remove_queen()

bfs()
