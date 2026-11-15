class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        trend = []
        for i in range(len(temperatures)):
            while trend and temperatures[i] > trend[-1][0]:
                temp, ind = trend.pop()
                res[ind] = i - ind
            trend.append((temperatures[i], i))
        return res