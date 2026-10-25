class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def areafinder(r,c):
            if (r,c) in visited or r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == 0:
                return 0

            visited.add((r,c))
            curr = 1
            for (dr,dc) in directions:
                curr += areafinder(r+dr, c+dc)

            return curr

        for r in range(rows):
            for c in range(cols):
                ans = areafinder(r,c)
                area = max(area,ans)

        return area