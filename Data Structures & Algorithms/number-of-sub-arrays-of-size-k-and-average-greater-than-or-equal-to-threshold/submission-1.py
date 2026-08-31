class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        movingSum = sum(arr[:k])
        ans = 0
        if movingSum//k >= threshold:
            ans += 1
        for i in range(k,len(arr)):
            print(movingSum)
            movingSum += arr[i]
            movingSum -= arr[i-k]
            if movingSum//k >= threshold:
                ans += 1
        
        return ans