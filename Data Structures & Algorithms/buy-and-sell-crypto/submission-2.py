class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = None
        max_price = None
        for p in prices:
            if min_price is None:
                min_price = max_price = p
            else:
                if p < min_price:
                    profit = max(max_price - min_price, profit)
                    min_price = max_price = p
                elif p > max_price:
                    max_price = p
            print(f"price: {p}, min: {min_price}, max: {max_price}, profit: {profit}")
        return max(profit, max_price - min_price)