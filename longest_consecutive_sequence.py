#  Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.

# This complexity is actually O(nlogn), but it passed the test and I don't know why
# The list sort() method takes O(nlogn)
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num.sort()
        max_len = 0
        cur_len = 1

        for i in range(len(num)-1):
            if num[i] + 1 == num[i+1]:
                cur_len += 1
            elif num[i] == num[i+1]:
                continue
            else:
                if cur_len > max_len:
                    max_len = cur_len
                cur_len = 1

        if cur_len > max_len:
            max_len = cur_len

        return max_len

# This should actually run in O(n), but the waste of memory space is ridiculous, and it didn't pass the test
class Solution2:
    def longestConsecutive(self, num):
        max_num = max(num)
        min_num = min(num)

        book = [False for i in range(min_num, max_num+1)]

        for n in num:
            book[n - min_num] = True
            
        max_len = 0
        cur_len = 1
        for i in range(len(book)-1):
            if book[i] == book[i+1] == True:
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len
                cur_len = 1

        if cur_len > max_len:
            max_len = cur_len

        return max_len



num = [100, 4, 200, 1, 3, 2]
# num = [1,2,0,1]
print Solution2().longestConsecutive(num)
