class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first, second = -1 * heapq.heappop(heap), -1 *heapq.heappop(heap)
            new = abs(first-second)
            heapq.heappush(heap, -1*new)
        return abs(heap[0])
