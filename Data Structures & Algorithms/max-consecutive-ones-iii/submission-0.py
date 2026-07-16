class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0 
        ans = 0
        zeroFlipped = k

        while right < len(nums):
            if nums[right] == 0:
                zeroFlipped -= 1
            
            while zeroFlipped < 0:
                if nums[left] == 0:
                    zeroFlipped += 1
                left += 1
            
            ans = max(ans, (right-left+1))
            right += 1

        return ans
                
                 