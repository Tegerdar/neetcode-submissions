class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = float('inf')
        profit = 0
        for p in prices:
            buyPrice = min(buyPrice, p)
            profit = max(profit, p - buyPrice)
        return profit