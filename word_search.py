#  Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   ["ABCE"],
#   ["SFCS"],
#   ["ADEE"]
# ]
#
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
class Solution:
    # @param board, a list of lists of 1 lenght string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not board or not board[0] or not word:
            return False

        # board = [row[0] for row in board]
        self.board = board
        self.word = word

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.find((i,j), 0, []):
                    return True
        else:
            return False


    def find(self, (i, j), k, path):
        if self.board[i][j] == self.word[k]:
            if k == len(self.word) - 1:
                return True
            else:
                # Find adjacent positions
                path.append((i,j))
                to_find = []

                for (n_i, n_j) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if 0 <= n_i < len(self.board) and 0 <= n_j < len(self.board[0]) and (n_i, n_j) not in path:
                            to_find.append((n_i, n_j))

                for pos in to_find:
                    if self.find(pos, k+1, path):
                        return True
                else:
                    path.pop()
                    return False
        else:
            return False

board = [
    "aa"
]

word = "aa"

print Solution().exist(board, word)
