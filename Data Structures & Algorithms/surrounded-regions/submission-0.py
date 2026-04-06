class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def convert():
            q = deque()

            for r in range(rows):
                for c in range(cols):
                    if (r == 0 or r == rows-1) or (c == 0 or c == cols-1) and board[r][c] == "O":
                        q.append((r,c))

            while q:
                r, c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "U"
                    for dr,dc in directions:
                        if 0 <= dr+r < rows and 0 <= dc+c < cols:
                            q.append((dr+r, dc+c))
        convert()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "U":
                    board[r][c] = "O"
        