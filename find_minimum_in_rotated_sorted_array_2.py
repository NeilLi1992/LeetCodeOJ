# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# The array may contain duplicates.

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        minimum = float('inf')
        for i in num:
            if i < minimum:
                minimum = i

        return minimum

print Solution().findMin([1])
