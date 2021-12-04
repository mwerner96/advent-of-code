class Board:
    def __init__(self, board):
        self.board = board

    def update(self, new):
        self.board = [
            [
                -1 if num == new else num
                for num
                in line
            ]
            for line
            in self.board
        ]
        return self.check() * new

    def check(self):
        sum = 0
        done = False
        for x in range(0, 5):
            sum_row = 0
            sum_col = 0
            for y in range(0, 5):
                sum_row += self.board[x][y]
                sum_col += self.board[y][x]
                sum += self.board[x][y] if self.board[x][y] != -1 else 0
            if sum_row == -5 or sum_col == -5:
                done = True
        return sum if done else 0


with open('input') as f:
    numbers = list(map(int, f.readline().strip().split(',')))
    b = f.readlines()
    rawboards = [b[x+1:x+6] for x in range(0, len(b), 6)]
    boards = [
        Board([
            list(map(int, line.split()))
            for line
            in raw
        ])
        for raw
        in rawboards
    ]

for num in numbers:
    for board in boards:
        val = board.update(num)
        if val != 0:
            print(val)
            exit()
