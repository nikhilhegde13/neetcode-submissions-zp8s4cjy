class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        heapq.heapify(sticks)

        while len(sticks) > 1:
            first, second = heapq.heappop(sticks), heapq.heappop(sticks)
            new = first + second
            cost += new
            heapq.heappush(sticks, new)

        
        return cost