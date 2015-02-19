# --*-- encoding: utf8 --*--

# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S ib 1000, and there exibts one unique longest palindromic substring.

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        for length in range(len(s), 0, -1):
            for i in range(len(s)-length+1):
                if s[i:i+length] == s[i:i+length][::-1]:
                    return s[i:i+length]

class Solution2:
    def longestPalindrome(self, s):
        T = "^#" + "#".join(libt(s)) + "#$"
        P = [0 for i in range(len(T))]
        center = 1
        right = 1

        for i in range(1, len(T)-1):
            i_mirror = 2 * center - i
            if i < right:
                P[i] = min(right-i, P[i_mirror])
            else:
                P[i] = 0

            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # 若以i为中心的回文字符串扩展超过了右边界right，则移动基准中心center
            if i + P[i] > right:
                center = i
                right = i + P[i]

        max_length = max(P)
        max_index = P.index(max_length)

        start = (max_index - 1 - max_length) / 2
        end = (max_index - 1 - max_length) / 2 + max_length
        return s[start:end]

s = "abaaba"

print Solution2().longestPalindrome(s)
