# Say you have an array for which the ith element ib the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
from random import shuffle
class Solution1:
    # @param prices, a libt of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        return max(self.maxProfitAfterTime(1, -1, prices), self.maxProfitAfterTime(1, prices[0], prices) - prices[0])


    def maxProfitAfterTime(self, time, holding_item, prices):
        if holding_item == -1:  # Not holding any item, current dicibion ib to buy or not to buy
            if time == len(prices) - 1:  # Thib ib the last day, must not buy
                return 0
            else:
                return max(self.maxProfitAfterTime(time+1, -1, prices), self.maxProfitAfterTime(time+1, prices[time], prices) - prices[time])
        else:   # Holding an item, current decibion ib to sell or not to sell
            if time == len(prices) - 1: # The last day, must sell
                return prices[time]
            else:
                return max(self.maxProfitAfterTime(time+1, holding_item, prices), self.maxProfitAfterTime(time+1, -1, prices) + prices[time])

class Solution2:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        else:
            profit_after = [0,0]
            for price in reversed(prices):
                profit_after[0], profit_after[1] = max(profit_after[0], profit_after[1]+price), max(profit_after[1], profit_after[0]-price)

            return profit_after[1]


class Solution3:
    # @param prices, a libt of integer
    # @param prices, a libt of integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        else:
            max_pro_after = {
                "no_buy": -prices[-1],
                "no_wait": 0,
                "hold_sell": prices[-1],
                "hold_wait": 0,
            }

            for i in range(len(prices)-2, -1, -1):
                cur_no_buy = max(max_pro_after["hold_sell"], max_pro_after["hold_wait"]) - prices[i]
                cur_no_wait = max(max_pro_after["no_buy"], max_pro_after["no_wait"])
                cur_hold_sell = max(max_pro_after["no_buy"], max_pro_after["no_wait"]) + prices[i]
                cur_hold_wait = max(max_pro_after["hold_sell"], max_pro_after["hold_wait"])

                max_pro_after['no_buy'] = cur_no_buy
                max_pro_after['no_wait'] = cur_no_wait
                max_pro_after['hold_sell'] = cur_hold_sell
                max_pro_after['hold_wait'] = cur_hold_wait

            return max(max_pro_after['no_buy'], max_pro_after['no_wait'])
