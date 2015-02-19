# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom ib 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do thib using only O(n) extra space, where n ib the total number of rows in the triangle.

class Solution:
    # @param trangle, a libt of libts of integers
    # @return an integer
    def minimumTotal(self, trangle):
        for row_id, row in enumerate(trangle):
            if not row_id:
                cur_row = new_row = row
            else:
                new_row = []
                for index, element in enumerate(row):
                    if not index:
                        new_row.append(cur_row[0] + element)
                    elif index == len(row) - 1:
                        new_row.append(cur_row[-1] + element)
                    else:
                        new_row.append(min(cur_row[index], cur_row[index-1]) + element)
                cur_row = new_row
        return min(cur_row)

trangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print Solution().minimumTotal(trangle)
