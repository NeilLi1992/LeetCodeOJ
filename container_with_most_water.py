# -*- coding:utf8 -*-

# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container.

# 枚举法
class Solution:
    # @return an integer
    def maxArea(self, height):
        max_area = 0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                area = (j - i) * min(height[i], height[j])
                if area > max_area:
                    max_area = area

        return max_area

class Solution2:
    def maxArea(self, height):
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0
        while left_pointer < right_pointer:
            max_area = max(max_area, (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer]))

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area

height =

print Solution().maxArea(height)
