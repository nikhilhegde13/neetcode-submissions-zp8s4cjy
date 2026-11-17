class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        res = high

        def shipping(cap):
            ships, curr = 1, cap

            for w in weights:
                if curr-w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    curr = cap
                curr -= w
            return True

        while low <= high:
            mid = (low+high)//2

            if shipping(mid):
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return res