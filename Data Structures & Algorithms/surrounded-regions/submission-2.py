class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def capture(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == "X" or board[r][c] == "F":
                return
            
            board[r][c] = "F"

            for dr,dc in directions:
                capture(r+dr, c+dc)
            
            return 
        
        for r in range(rows):
            capture(r,0)
            capture(r,cols-1)
        for c in range(cols):
            capture(0,c)
            capture(rows-1,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "F":
                    board[r][c] = "O"