class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k

        def quickSelect(start, end):
            while True:
                if start == end:
                    return nums[start]
                
                # Pick a random pivot to avoid O(n^2) worst case on sorted arrays
                pivot_idx = random.randint(start, end)
                nums[pivot_idx], nums[end] = nums[end], nums[pivot_idx]
                
                left = start
                pivot = nums[end]

                for i in range(start, end):
                    if nums[i] <= pivot:
                        nums[left], nums[i] = nums[i], nums[left]
                        left += 1
                
                nums[left], nums[end] = nums[end] , nums[left]

                if left > k:
                    end = left - 1
                elif left < k:
                    start = left + 1
                else:
                    return nums[left]

        import random
        return quickSelect(0,len(nums)-1)