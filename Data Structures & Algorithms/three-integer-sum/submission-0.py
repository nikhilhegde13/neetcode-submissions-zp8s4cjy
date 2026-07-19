class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            
            if i > 0 and nums[i-1] == num:
                continue 

            left, right = i+1, len(nums)-1
            while left < right:
                ts = num + nums[left] + nums[right]

                if ts == 0:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif ts < 0:
                    left += 1
                else:
                    right -= 1
        return ans