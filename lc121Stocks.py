# LeetCode #121 Best Time to Buy and Sell Stock
# Accepted 212 / 212 testcases passed

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            min_price = float('inf')
            max_profit = 0
            for price in prices:
    # update min_price if current price is lower
                if price < min_price:
                    min_price = price
    # calculate profit at current price
                profit = price - min_price
    # update max_profit if current profit is higher
                if profit > max_profit:
                    max_profit = profit
            return max_profit