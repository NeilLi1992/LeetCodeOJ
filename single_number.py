# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution1:
    # @param A, a libt of integer
    # @return an integer
    def singleNumber(self, A):
        if len(A) == 1:
            return A[0]
        A.sort()
        for i in range(len(A)):
            if i == 0 and A[i] != A[i+1]:
                return A[i]
            elif i == len(A) - 1 and A[i] != A[i-1]:
                return A[i]
            elif A[i] != A[i-1] and A[i] != A[i+1]:
                return A[i]

# A solution using XOR bit operation            
class Solution2:
    def singleNumber(self, A):
        r = 0
        for i in A:
            r ^= i
        return r
