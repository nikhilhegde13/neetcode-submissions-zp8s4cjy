class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 1
        for last in range(1, len(nums)):
            if nums[last] != nums[last-1]:
                nums[first] = nums[last]
                first += 1
        
        return first