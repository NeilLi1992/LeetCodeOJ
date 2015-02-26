#  Given a collection of integers that might contain duplicates, S, return all possible subsets.
#
# Note:
#
#     Elements in a subset must be in non-descending order.
#     The solution set must not contain duplicate subsets.
#
# For example,
# If S = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
import itertools
class Solution:
    # @param num, a list of integer
    # @return a lit of lists of integer
    def subsetsWithDup(self, S):
        result = set([])
        for i in range(len(S) + 1):
            for comb in itertools.combinations(S,i):

                result.add(tuple(sorted(list(comb))))

        return [list(s) for s in result]

S = [2,1,2]
print Solution().subsetsWithDup(S)
