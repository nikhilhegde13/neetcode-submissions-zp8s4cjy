class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = 0
        for ops in logs:
            if ops == "../":
                if stack:
                    stack -= 1
            elif ops == "./":
                pass
            else:
                stack += 1
        
        return stack