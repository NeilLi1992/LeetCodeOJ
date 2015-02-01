# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution:
    # @param prices, alist of integr
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        before_min = prices[0]
        max_profit = 0
        for price in prices:
            if price - before_min > max_profit:
                max_profit = price- before_min

            if price < before_min:
                before_min = price
        return max_profit


prices = [4,1,2,6,4,10,5,1]
print Solution().maxProfit(prices)
