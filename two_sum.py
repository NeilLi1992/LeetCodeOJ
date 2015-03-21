# Given an array of integers, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        for index1 in range(0, len(num) - 1):
            for index2 in range(index1+1, len(num)):
                if num[index1] + num[index2] == target:
                    return (index1+1, index2+1)

class Solution2:
    def twoSum(self, num, target):
        self.num = num
        self.sort_num = sorted(num)
        self.target = target
        for i in range(len(num)):
            if self.binarySearch(target - num[i], 0, len(num)) != None:
                index1 = i + 1
                for j in range(i+1, len(num)):
                    if num[j] == target - num[i]:
                        index2 = j + 1
                        return (index1, index2)

    def binarySearch(self, n, start, end):
        if start >= end:
            return None
        else:
            mid = (start + end) / 2
            if n == self.sort_num[mid]:
                return mid
            elif n < self.sort_num[mid]:
                return self.binarySearch(n, start, mid)
            else:
                return self.binarySearch(n, mid+1, end)

target = 16021
print Solution2().twoSum(numbers, target)
