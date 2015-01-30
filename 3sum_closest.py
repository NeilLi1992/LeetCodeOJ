# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()

        if len(num) < 3:
            return returnList
        else:
            global_difference = float("inf")
            global_sum = 0
            for i in range(len(num)-2):
                if i > 0 and num[i] == num[i-1]:
                    continue # This num is equal to previous num, skip it
                else:
                    #
                    num1 = num[i]
                    # remainder = 0 - num1 # This is what we need to find
                    begin = i + 1
                    end = len(num) - 1
                    while begin < end:
                        num2 = num[begin]
                        num3 = num[end]

                        local_sum = num1 + num2 + num3
                        local_difference = abs(local_sum - target)

                        if local_difference < global_difference:
                            global_difference, global_sum = local_difference, local_sum
                        if local_sum < target:
                            # Move begin to next position
                            begin += 1
                            while begin < end and num[begin] == num[begin-1]:
                                begin += 1
                        elif local_sum > target:
                            # Move end to next position
                            end -= 1
                            while begin < end and num[end] == num[end+1]:
                                end -= 1
                        else:   # The difference is zero, can't be smaller
                            return local_sum

            return global_sum
