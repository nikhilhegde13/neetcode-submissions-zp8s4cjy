class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        left, right = 0, 0 
        zeroes = 0

        while right < len(nums):
            if nums[right] == 0:
                zeroes += 1
            
            while zeroes == 2:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            
            ans = max(ans, right-left+1)
            right += 1
        
        return ans