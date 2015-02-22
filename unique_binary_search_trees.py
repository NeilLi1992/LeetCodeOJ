# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution:
    # @return an integer
    def numTrees(self, n):
        G = [1, 1]

        for i in xrange(2, n+1):
            G.append(0)
            for j in xrange(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]

print Solution().numTrees(2)
