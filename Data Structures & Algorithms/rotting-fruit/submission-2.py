class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh, time = 0, 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while fresh > 0 and q:
            l = len(q)
            for curr in range(l):
                r, c = q.popleft()

                for dr, dc in directions:
                    if (0 <= (r+dr) < rows and 0 <= (c+dc) < cols) and grid[r+dr][c+dc] == 1:
                        grid[r+dr][c+dc] = 2
                        q.append((r+dr, c+dc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
