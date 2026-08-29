class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        ans = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
               ans = max(ans, (prices[sell]-prices[buy]))
            else:
                buy = sell
            sell += 1
        
        return ans