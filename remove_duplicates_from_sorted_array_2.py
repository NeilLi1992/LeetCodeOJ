#  Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array A = [1,1,1,2,2,3],
#
# Your function should return length = 5, and A is now [1,1,2,2,3].

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        new = []
        i = 0
        while i < len(A):
            new.append(A[i])
            if i < len(A) - 1 and A[i] == A[i+1]:
                new.append(A[i])

            while i < len(A) - 1 and A[i+1] == A[i]:
                i += 1
            i += 1

        for i in xrange(len(new)):
            A[i] = new[i]

        return len(new)

A = [1,1,1,2,2,3]
print Solution().removeDuplicates(A)
print A
