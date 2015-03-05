#  Given a set of distinct integers, S, return all possible subsets.
#
# Note:
#
#     Elements in a subset must be in non-descending order.
#     The solution set must not contain duplicate subsets.
#
# For example,
# If S = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
import itertools
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        result = []
        for i in range(len(S)+1):
            for l in [sorted(list(c)) for c in itertools.combinations(S, i)]:
                result.append(l)

        return result

S = [1,2,3]
print Solution().subsets(S)
