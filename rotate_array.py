# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    def rotate(self, nums, k):
        if not nums:
            return nums
        else:
            for i in xrange(k):
                temp = nums.pop()
                nums.insert(0, temp)

class Solution2:
    def rotate(self, nums, k):
        nums.reverse()
        print nums
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

nums = [1,2,3,4,5,6,7]
k = 3
Solution2().rotate(nums,k)
print nums
