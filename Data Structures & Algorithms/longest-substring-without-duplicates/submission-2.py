class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0,0
        curr = set(s[start:end])
        anslen = 0

        while end < len(s) and start <= end:
            while s[end] in curr:
                curr.remove(s[start])
                start += 1
            curr.add(s[end])
            anslen = max(anslen, end - start + 1)
            end += 1

        return anslen




