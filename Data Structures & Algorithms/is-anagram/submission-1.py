class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1
        
        for c in t:
            if c not in hashmap:
                return False
            if hashmap[c] == 0:
                return False
            if hashmap[c] > 0:
                hashmap[c] -= 1
        
        return True