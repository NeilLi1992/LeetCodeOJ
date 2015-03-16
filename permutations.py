#  Given a collection of numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
#
import itertools

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        to_return = []
        for t in itertools.permutations(num, len(num)):
            to_return.append(list(t))

        return to_return

print Solution().permute([1,2,3])
