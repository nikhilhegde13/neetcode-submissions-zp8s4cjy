class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        mod = 10**9 + 7

        right = len(nums)-1
        for i, left in enumerate(nums):
            while i <= right and left + nums[right] > target:
                right -= 1
            
            if i <= right:
                ans += pow(2, right - i, mod)
                ans %= mod

        return ans