class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini, maxi = 1, max(piles)
        res = maxi

        while mini <= maxi:
            k = (mini + maxi ) // 2

            time = 0

            for banana in piles:
                time += math.ceil((banana) /k )
            if time <= h:
                res = k 
                maxi = k - 1
            else:
                mini = k + 1
        
        return res