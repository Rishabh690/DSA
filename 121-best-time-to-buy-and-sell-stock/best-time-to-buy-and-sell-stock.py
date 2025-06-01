class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)

        return max_profit
