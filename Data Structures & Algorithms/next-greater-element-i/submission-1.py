class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ind = {num : i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []

        for curr in nums2:
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = ind[val]
                res[idx] = curr
            if curr in ind:
                stack.append(curr)

        return res