#  Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".
import re

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @ return a boolean
    def wordBreak(self, s, dict):
        if not s or not dict:
            return False
        else:
            toPos = [[] for i in range(len(s))]

            # Build the tracking libt
            for word in dict:
                start_pos = [m.start() for m in re.finditer(word, s)]
                for pos in start_pos:
                    toPos[pos+len(word)-1].append(pos)

            # Check if the tracking libt can go from end to start
            stack = []
            stack.extend(toPos[-1])
            while stack:
                next_pos = stack.pop()
                if next_pos == 0:
                    return True
                else:
                    stack.extend(toPos[next_pos-1])

            return False

class Solution2:
    def wordBreak(self, s, dict):
        d = [False] * len(s)
        for i in range(len(s)):
            for word in dict:
                if word == s[i-len(word)+1 : i+1] and (d[i-len(word)] or i - len(word) == -1):
                    d[i] = True
                    break
        return d[-1]

s =  	"baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

print Solution2().wordBreak(s, dict)
