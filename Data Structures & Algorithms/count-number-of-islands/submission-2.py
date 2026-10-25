class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        m = len(grid)
        n = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(row, col):
            if (row, col) in visited or row >= m or col >= n or row < 0 or col < 0 or grid[row][col] == "0":
                return 0

            visited.add((row,col))
            
            for dr, dc in directions:
                dfs(row + dr, col + dc)

            return 1

        for r in range(m):
            for c in range(n):
                islands += dfs(r, c)

        return islands

