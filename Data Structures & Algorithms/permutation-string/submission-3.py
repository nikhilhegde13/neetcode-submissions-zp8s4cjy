class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        first, target = [0] * 26, [0] * 26
        for c in s1:
            first[ord(c) - 97] += 1
        for i, c in enumerate(s2):
            target[ord(c) - 97] += 1                 # 
            if i >= n:
                target[ord(s2[i - n]) - 97] -= 1     # 
            if target == first:
                return True
        return False