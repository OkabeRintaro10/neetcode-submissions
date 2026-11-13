class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for sell in range(1, len(prices)):
            min_price = min(min_price, prices[sell])

            profit = max(profit, (prices[sell] - min_price))

        return profit