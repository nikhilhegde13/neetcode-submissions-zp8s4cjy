class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        chars = []
        ans = ""
        k = 0
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                chars.append(ans)
                nums.append(k)
                ans = ""
                k = 0
            elif c == "]":
                buffer = ans
                ans = chars.pop()
                count = nums.pop()
                ans += buffer * count
            else:
                ans += c
        
        return ans