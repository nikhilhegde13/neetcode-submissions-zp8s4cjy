class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Always satisfied, regardless of where the window goes.
        base = sum(c for c, g in zip(customers, grumpy) if not g)

        gain = best = 0
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            if g:
                gain += c                       
            if i >= minutes and grumpy[i - minutes]:
                gain -= customers[i - minutes]  
            best = max(best, gain)

        return base + best