class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import math
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        while k:
            k -= 1
            curr = -1 * heapq.heappop(gifts)
            heapq.heappush(gifts,-1*math.floor(math.sqrt(curr)))

        return abs(sum(gifts))