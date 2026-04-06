class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)]

        po = [[False] * cols for _ in range(rows)]
        ao = [[False] * cols for _ in range(rows)]

        pacific = []
        atlantic  = []

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr,dc in directions:
                    if (0 <= (dr+r) < rows) and (0 <= (dc+c) < cols) and heights[dr+r][dc+c] >= heights[r][c] and not ocean[dr+r][dc+c]:
                        q.append((dr+r, dc+c))

        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows-1,c))

        for r in range(rows):
            pacific.append((r,0))
            atlantic.append((r,cols-1))
        
        bfs(pacific, po)
        bfs(atlantic,ao)

        res = []
        for r in range(rows):
            for c in range(cols):
                if po[r][c] and ao[r][c]:
                    res.append([r,c])
        return res
