class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]

        for i in range(len(nums)):
            left = prefix[i]
            right = prefix[len(nums)] - prefix[i+1]
            if left == right:
                return i 

        return -1