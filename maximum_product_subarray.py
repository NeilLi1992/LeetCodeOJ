#  Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

# Enumeration
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        maxProduct = -float("inf")
        for i in range(len(A)):
            product = 1
            for j in range(i, len(A)):
                product *= A[j]

                if product > maxProduct:
                    maxProduct = product

                if product == 0:
                    break

        return maxProduct

# Dynamic programming
class Solution2:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        maxProduct = -float("inf")
        products = [[1 for j in range(len(A))] for i in range(len(A))]

        for length in range(len(A)):
            for start in range(len(A)-length):
                if length == 0:
                    products[start][start] = A[start]
                else:
                    products[start][start+length] = products[start][start+length-1] * products[start+length][start+length]

                    if products[start][start+length] > maxProduct:
                        maxProduct = products[start][start+length]

        return maxProduct



A = [2,3,-2,4]

print Solution2().maxProduct(A)
