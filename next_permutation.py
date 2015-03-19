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

import itertools

class Solution:
    def nextPermutation(self, num):
        str_digit_list = [str(n) for n in num]
        permu_list = list(itertools.permutations(str_digit_list))
        num_list = sorted([int("".join(t)) for t in permu_list])
        tuple_list = [tuple(self.split_num(n)) for n in num_list]

        index = tuple_list.index(tuple(num))
        num[:] = []
        if index == len(tuple_list) - 1:
            num.extend(tuple_list[0])
        else:
            num.extend(tuple_list[index+1])

    def split_num(self, num):
        digit_list = []
        while num / 10:
            digit_list.append(num % 10)
            num /= 10
        digit_list.append(num % 10)
        digit_list.reverse()
        return digit_list

class Solution2:
    # @paramnum, a list of integer
    # @erturn nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        max_n = -float("inf")
        max_i = -1
        for i in range(len(num)-1, -1, -1):
            n = num[i]
            if n >= max_n:
                max_n = n
                max_i = i
                continue
            else:
                # This num is not the largest num we've met, find the one slightly larger than it on its right side
                larger_index = -1
                larger_num = -float("inf")
                for j in range(len(num)-1, i, -1):
                    if num[j] > n:
                        larger_index = j
                        larger_num = num[j]
                        break
                num[i+1:larger_index+1] = num[i:larger_index]
                num[i] = larger_num
                num[i+1:] = sorted(num[i+1:])

                # We are done
                break
        else:
            num.reverse()



# num = [1,3,2]
# Solution().nextPermutation(num)
# print num
num = [2,3,1]
Solution2().nextPermutation(num)
print num
