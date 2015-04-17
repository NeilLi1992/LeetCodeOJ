#  Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.
#

class Solution:
    # @param height, an integer[]
    # @return an integer
    def largestRectangleArea(self, height):
        rec_stack = []
        max_area = 0

        for i,h in enumerate(height):
            # Check if this ends previous rectanlges
            modified = False
            while rec_stack and rec_stack[-1][1] > h:
                modified = True
                index, rec_height = rec_stack.pop()
                new_index = index
                if (i - index) * rec_height > max_area:
                    max_area = (i - index) * rec_height

            if modified:
                new_height = h
                rec_stack.append((new_index, new_height))

            # If not, push this into stack
            if not modified:
                rec_stack.append((i,h))

        print rec_stack
        # Check the rest rectangles
        for i,h in rec_stack:
            if (len(height) - i) * h > max_area:
                max_area = (len(height) - i) * h

        return max_area

height = [1,1,1,1,1,1,2,1,1,1,1,1,1]
print Solution().largestRectangleArea(height)
