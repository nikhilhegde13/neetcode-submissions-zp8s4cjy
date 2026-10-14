class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0

        for i in range(len(nums)):
            if nums[i] :
                nums[i], nums[first] = nums[first], nums[i]
                first += 1
            print(nums)

        