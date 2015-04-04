#  Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        container_split_list = []
        left_split = right_split = max_basin_height = 0

        for i,n in enumerate(A):
            if n <= max_basin_height or n >= A[left_split]:
                # A container is formed
                container_split_list.append(left_split, i)
            else:
                pass

    def trap(self, A):
        split_list = []
        left_split = left = 0
        right_split = right = len(A) - 1
        max_split_height = max(A[left_split], A[right_split])

        while left < right:
            pass

class Solution2:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        self.A = A
        self.container_list = []
        self.searchInRange(0, len(A)-1)
        # All contianers are identified
        total_rain = 0
        for left,right in self.container_list:
            if right - left > 1:
                max_water_height = min(A[left], A[right])
                for i in range(left+1, right):
                    total_rain += max_water_height - A[i]
        return total_rain

    def searchInRange(self, left, right):
        if right - left <= 1:
            return
        else:
            if self.A[left] <= self.A[right]:
                # Go from left to right
                for i in range(left+1, right):
                    if self.A[i] >= self.A[left]:
                        # (left, i) must be a container
                        self.container_list.append((left, i))
                        self.searchInRange(i, right)
                        return
                else:
                    # (left, right) can be a container
                    self.container_list.append((left, right))
            else:
                # Go from right to left
                for i in range(right-1, left, -1):
                    if self.A[i] >= self.A[right]:
                        # (i, right) must be a container
                        self.container_list.append((i, right))
                        self.searchInRange(left, i)
                        return
                else:
                    # (left, right) can be a container
                    self.container_list.append((left, right))

A = [0,1,0,2,1,0,1,3,2,1,2,1]
print Solution2().trap(A)
