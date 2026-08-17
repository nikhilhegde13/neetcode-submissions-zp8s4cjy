class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        ans = -1
        for i in range(len(nums)-1):
            second = i+1
            while second < len(nums):
                print(i,second)
                print(nums[i] + nums[second])
                if nums[i] + nums[second] < k:
                    ans = max(ans, (nums[i] + nums[second])) 
                second += 1
        
        return ans