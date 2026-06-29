class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        res = curr = 0

        for num in nums:
            curr += num
            diff = curr - k

            res += prefixSum.get(diff, 0)
            prefixSum[curr] = 1 + prefixSum.get(curr,0)

        return res