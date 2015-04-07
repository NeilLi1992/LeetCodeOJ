#  Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# a) Insert a character
# b) Delete a character
# c) Replace a character

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        edit = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for j in range(len(word2)+1):
            edit[0][j] = j

        for i in range(len(word1)+1):
            edit[i][0] = i

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    edit[i][j] = min(edit[i-1][j] + 1, edit[i][j-1] + 1, edit[i-1][j-1])
                else:
                    edit[i][j] = min(edit[i-1][j] + 1, edit[i][j-1] + 1, edit[i-1][j-1] + 1)

        return edit[-1][-1]


word1 = "abcdxabcdasde"
word2 = "qwkyokasd"
print Solution().minDistance(word1, word2)
