class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        trans = 0
        curr = 0
        for id in transactions:
            curr += id
            if curr >= 0:
                trans += 1
            else:
                curr -= id
            
        return trans