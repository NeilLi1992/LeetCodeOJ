#  Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array A = [1,1,2],
#
# Your function should return length = 2, and A is now [1,2].

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        else:
            index = 0
            while index < len(A) - 1:
                while A.count(A[index]) > 1:
                    del A[index]
                index += 1
            return len(A)

class Solution2:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        else:
            count = dict()
            for n in A:
                c = count.get(n, 0)
                count[n] = c + 1

            for key, value in count.iteritems():
                while value > 1:
                    A.remove(key)
                    value -= 1

            return len(A)

class Solution3:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        new = sorted(list(set(A)))
        for i in xrange(len(new)):
            A[i] = new[i]
        length = len(new)
        return length

A = [1,1,2]
print Solution3().removeDuplicates(A)
print A
