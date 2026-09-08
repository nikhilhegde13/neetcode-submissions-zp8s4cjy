class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            while len(count) > k:
                out = s[left]
                count[out] -= 1
                if count[out] == 0:
                    del count[out]
                left += 1
            best = max(best, right - left + 1)
        return best