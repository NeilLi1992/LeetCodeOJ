# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        replace = {}

        for i,c in enumerate(s):
            if c not in replace:
                if t[i] not in replace.values():
                    replace[c] = t[i]
                else:
                    return False
            else:
                if replace[c] != t[i]:
                    return False
        else:
            return True

print Solution().isIsomorphic('egg', 'add')
print Solution().isIsomorphic('foo', 'bar')
print Solution().isIsomorphic('paper', 'title')
print Solution().isIsomorphic('13', '14')
print Solution().isIsomorphic('ab', 'aa')
