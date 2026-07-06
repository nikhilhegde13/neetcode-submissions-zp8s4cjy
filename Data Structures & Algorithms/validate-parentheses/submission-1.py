class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        comb = { "(":")", "{":"}", "[": "]"}
        for c in s:
            if c in ["}", ")", "]"]:
                if stack and c == comb[stack[-1]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        
        return False if len(stack) else True