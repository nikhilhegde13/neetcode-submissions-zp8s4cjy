class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific , atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def flows(r, c, visited, last):
            if (r,c) in visited or r == rows or r < 0 or c < 0 or c == cols or heights[r][c] < last:
                return 

            visited.add((r,c))
            for dr,dc in directions:
                flows(r+dr, c+dc, visited, heights[r][c])

        for r in range(rows):
            flows(r, 0, pacific, heights[r][0])
            flows(r, cols-1, atlantic, heights[r][cols-1])

        for c in range(cols):
            flows(0, c, pacific, heights[0][c])
            flows(rows-1, c, atlantic, heights[rows-1][c])
            
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res