class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1

        while left < right:
            tots = nums[left] + nums[right]
            if tots == target:
                return [left+1, right+1]
            elif tots > target:
                right -= 1
            else: 
                left += 1
        