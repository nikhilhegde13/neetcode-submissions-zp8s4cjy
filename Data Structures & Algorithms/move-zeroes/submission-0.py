class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        f = 0
        for l in range(len(nums)):
            if nums[l]:
                nums[f], nums[l] = nums[l], nums[f]
                f += 1
        