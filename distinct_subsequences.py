#  Given a string S and a string T, count the number of distinct subsequences of T in S.
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
#
# Return 3.

# Slow recursive solution
class Solution1:
    # @return an integer
    def numDistinct(self, S, T):
        if not len(S):
            return 1 if not len(T) else 0

        if not len(T):
            return 1

        distinct_count = 0

        next_T = T[1:]
        for i in range(0, len(S)):
            if S[i] == T[0]:
                distinct_count += self.numDistinct(S[i+1:], next_T)

        return distinct_count

print Solution1().numDistinct("rabbbit", "rabbit")
