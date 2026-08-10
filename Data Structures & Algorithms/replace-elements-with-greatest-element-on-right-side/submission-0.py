class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1] * len(arr)

        for i in range(len(ans)-2,-1,-1):
            ans[i] = max(arr[i+1], ans[i+1])
        

        return ans