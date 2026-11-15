class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        chars = []
        ans = ""
        carry = 0

        for c in s:
            if c.isdigit():
                carry = carry * 10 + int(c)
            elif c == "[":
                chars.append(ans)
                nums.append(carry)
                ans = ""
                carry = 0
            elif c == "]":
                temp = ans
                ans = chars.pop()
                count = nums.pop()
                ans += temp * count
            else:
                ans += c

        return ans
