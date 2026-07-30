class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        affordable = []
        i = 0

        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(affordable, -projects[i][1])
                i += 1
            if not affordable:
                break                              
            w -= heapq.heappop(affordable)
        return w