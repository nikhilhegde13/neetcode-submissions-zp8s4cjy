class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num,i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        while k:
            k -= 1
            new,i = heapq.heappop(heap)
            nums[i] *= multiplier
            heapq.heappush(heap,(nums[i], i))
        
        return nums