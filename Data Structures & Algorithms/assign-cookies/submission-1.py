class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        child = 0
        cookie = 0
        s.sort()
        g.sort()
        while cookie < len(s) and child < len(g):
            if s[cookie] >= g[child]:
                ans += 1
                child += 1
            cookie += 1
        
        return ans