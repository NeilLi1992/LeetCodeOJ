# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        num.insert(0,0)
        num.insert(0,0)
        take_max = [0,0]
        not_take_max = [0,0]

        for i in range(2, len(num)):
            take_max.append(num[i] + max(take_max[i-2], not_take_max[i-2]))
            not_take_max.append(max(take_max[i-1], not_take_max[i-1]))

        return max(take_max[-1], not_take_max[-1])

num = [100, 1, 200, 1000]
print Solution().rob(num)
