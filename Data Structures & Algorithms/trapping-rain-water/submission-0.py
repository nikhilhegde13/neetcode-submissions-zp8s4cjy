class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0] * len(height)
        maxright = [0] * len(height)
        maxleft[0] = height[0]
        maxright[-1] = height[-1]

        for i in range(1, len(height)):
            maxleft[i] = max(maxleft[i-1], height[i])
        
        for i in range(len(height)-2,-1,-1):
            maxright[i] = max(maxright[i+1], height[i])

        res = 0
        for i in range(len(height)):
            res += min(maxleft[i], maxright[i]) - height[i]


        return res