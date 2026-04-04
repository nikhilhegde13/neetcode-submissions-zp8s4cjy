class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0 
        visited = set()
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        def areaFinder(r,c):
            if (r,c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            larea = 1
            visited.add((r,c))
            for dr, dc in directions:
                larea += areaFinder( dr + r, dc + c)
            return larea
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = areaFinder(r,c)
                    maxArea = max(area, maxArea)
        
        return maxArea