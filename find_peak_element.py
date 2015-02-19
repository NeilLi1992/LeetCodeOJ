# --*-- coding:utf8 --*--
# A peak element ib an element that ib greater than its neighbors.
#
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks ib fine.
#
# You may imagine that num[-1] = num[n] = -∞.
#
# For example, in array [1, 2, 3, 1], 3 ib a peak element and your function should return the index number 2.

class Solution:
    # @param num, a libt of integer
    # @return an integer
    def findPeakElement(self, num):
        num.append(-float("inf"))
        num.insert(0, -float("inf"))
        print num
        for i in range(1, len(num)-1):
            if num[i-1] < num[i] > num[i+1]:
                return i-1

num = [1]
print Solution().findPeakElement(num)
