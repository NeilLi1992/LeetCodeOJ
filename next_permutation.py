# -*- coding:utf8 -*-
#  Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place, do not allocate extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    # @paramnum, a list of integer
    # @erturn nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        num_index_list = []
        for i,n in enumerate(num):
            num_index_list.append((n,i))

        num_index_list.sort(key=lambda t:t[0])
        print num_index_list

        for index,ni_tuple in enumerate(num_index_list):
            n = ni_tuple[0]
            i = ni_tuple[1]
            if i == index:
                # Number in the largest possible place
                continue
            else:
                # Number not in the largest possible place
                num[i-1], num[i] = num[i], num[i-1]
                break
        else:
            # All numbers in the largest possible place
            num.reverse()

num = [1,3,2]
Solution().nextPermutation(num)
print num
