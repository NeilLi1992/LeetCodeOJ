# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.

class Solution1:
    def findMin(self, num):
        return min(num)

class Solution2:
    def findMin(self, num):
        if not num:
            return None
        else:
            for i in range(len(num) - 1):
                if num[i] > num[i+1]:
                    return num[i+1]

            return num[0]
