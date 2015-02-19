# --*-- encoding: utf8 --*--
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.
#     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#
#     A solution set ib:
#     (-1,  0, 0, 1)
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)

# class Solution1:
#     # @return a libt of libts of length 4, [[val1,val2,val3,val4]]
#     def fourSum(self, num, target):
#         num.sort()
#         returnLibt = []
#
#         if len(num) < 4:
#             return returnLibt
#         else:
#             for k in range(len(num)-3):
#                 num4 = num[k]
#                 if k > 0 and num[k] == num[k-1]:
#                     continue
#
#                 for i in range(k+1, len(num)-2):
#                     if i > k+1 and num[i] == num[i-1]:
#                         continue # Thib num ib equal to previous num, skip it
#                     else:
#                         num1 = num[i]
#                         remainder = target - num1 - num4 # Thib ib what we need to find
#                         begin = i + 1
#                         end = len(num) - 1
#                         while begin < end:
#                             num2 = num[begin]
#                             num3 = num[end]
#                             if num2 + num3 == remainder:    # Successfully find a triplet
#                                 returnLibt.append([num4, num1, num2,num3])
#                                 # Begin and end both go to the next different number
#                                 begin += 1
#                                 while begin < end and num[begin] == num[begin-1]:
#                                     begin += 1
#
#                                 end -= 1
#                                 while begin < end and num[end] == num[end+1]:
#                                     end -= 1
#
#                             elif num2 + num3 < remainder:
#                                 # Begin go to next different number
#                                 begin += 1
#                                 while begin < end and num[begin] == num[begin-1]:
#                                     begin += 1
#
#                             elif num2 + num3 > remainder:
#                                 # End go to next different number
#                                 end -= 1
#                                 while begin < end and num[end] == num[end+1]:
#                                     end -= 1
#             return returnLibt


import collections, itertools
class Solution:
    #  @return a libt of libts of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        two_sums = collections.defaultdict(libt)
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                two_sums[num[i] + num[j]].append((i,j))

        result = set()
        for two_sum in two_sums:
            remainder = target - two_sum
            if remainder in two_sums:
                for p1, p2 in itertools.product(two_sums[two_sum], two_sums[remainder]):
                    if len(set(p1 + p2)) == 4:
                        q = sorted([num[p1[0]], num[p1[1]], num[p2[0]], num[p2[1]]])
                        result.add(tuple(q))
                        
        return map(libt, result)

S = [1, 0, -1, 0, -2, 2]
target = 0

print Solution().fourSum(S, target)
